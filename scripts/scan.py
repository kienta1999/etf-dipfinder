"""Scan the ETF universe for dips. Writes data/scan.csv, prints candidates (grouped by theme) + leaders.

is_dip = (price < SMA200  OR  dd_52w <= DD_MIN)  AND  rs_spy_3m < 0
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

# --- knobs ---
DD_MIN = -0.10          # at least this far off 52w high (fast dip)
MIN_DOLLAR_VOL = 5e6    # 20d avg $ volume; below = illiquid, dropped
SL_SIGMA = 1.5          # stop = SL_SIGMA monthly sigmas below entry (noise band; 2.0 if URA-class vol stops you out)
RISK = 0.01             # portfolio fraction risked per position → size_1pct = RISK / |sl_pct|
BENCH = "SPY"
TOP_THEMES = 15         # candidates = every dip in the 15 themes with the deepest best dip
OUT = Path(__file__).resolve().parent.parent / "data" / "scan.csv"

# A theme = funds the SAME headline moves (gold + gold miners, uranium + reactors). Cause/necessity/catalyst are
# researched once per theme; basket/price per fund. XLU/XLY share only the SPDR wrapper, so each sector is its own theme.
UNIVERSE = {
    "bench": "SPY QQQ IWM RSP MAGS",
    "tech": "XLK", "financials": "XLF", "health": "XLV", "energy": "XLE", "industrials": "XLI",
    "discretionary": "XLY", "staples": "XLP", "utilities": "XLU", "materials": "XLB", "realestate": "XLRE", "comms": "XLC",
    "semis": "SMH SOXX XSD PSI DRAM",
    "software": "IGV WCLD SKYY",
    "cyber": "CIBR HACK BUG",
    "ai/robot": "BOTZ ROBO ARKQ AIQ BAI AIHY AIPO PHOX QTUM XT",
    "internet/ark": "FDN ARKK ARKW",
    "banks": "KRE KBE KBWB",
    "fin-other": "IAI IAK FINX ARKF",
    "crypto-spot": "IBIT ETHA",
    "crypto-equity": "BLOK BKCH WGMI",
    "biotech": "XBI IBB ARKG GNOM",
    "health-other": "IHI XHE IHF XHS PPH",
    "oil/gas": "XOP OIH FCG AMLP USO",
    "nuclear": "URA URNM NLR",
    "base-metals": "COPX PICK XME",
    "rare-earth": "REMX",
    "lithium": "LIT",
    "gold": "GDX GDXJ GLD",
    "silver": "SIL SLV",
    "solar": "TAN",
    "clean": "ICLN QCLN PBW",
    "hydrogen": "HYDR",
    "wind": "FAN",
    "grid/infra": "GRID PAVE IGF",
    "defense-us": "ITA PPA XAR SHLD",
    "defense-eu": "EUAD",
    "space": "UFO ARKX",
    "transport": "JETS IYT",
    "housing": "XHB ITB",
    "consumer": "XRT PEJ BJK IBUY ONLN",
    "reit": "VNQ SRVR DTCR",
    "water": "PHO",
    "china": "KWEB FXI",
    "em": "EEM", "dev-exus": "EFA", "japan": "EWJ", "korea": "EWY", "taiwan": "EWT", "brazil": "EWZ",
    "india": "INDA", "argentina": "ARGT", "vietnam": "VNM",
}
THEME = {t: k for k, v in UNIVERSE.items() for t in v.split()}


def ret(px, n):
    return px.iloc[-1] / px.iloc[-1 - n] - 1 if len(px) > n else np.nan


def metrics(px, vol, spy):
    """One row of metrics for a single ETF. px/vol/spy are aligned Series."""
    px, vol = px.dropna(), vol.reindex(px.dropna().index)
    spy = spy.reindex(px.index).ffill()
    last = px.iloc[-1]
    roll_hi = px.rolling(252, min_periods=20).max()
    dd_series = px / roll_hi - 1
    dd = dd_series.iloc[-1]
    vol60 = px.pct_change().iloc[-60:].std() * np.sqrt(252)
    sma200 = px.iloc[-200:].mean() if len(px) >= 200 else np.nan
    sma50 = px.iloc[-50:].mean() if len(px) >= 50 else np.nan
    dip_low = px.loc[px.iloc[-252:].idxmax():].min()   # lowest close since the 52w high = thesis stop
    tp = 1 / (1 + dd) - 1                               # back to the 52w high; -27% dd is a +37% climb
    sl = -SL_SIGMA * vol60 / np.sqrt(12) if vol60 else np.nan
    return {
        "days": len(px),
        "price": last,
        "dd_52w": dd,
        "dd_pctile": (dd_series.dropna() <= dd).mean(),  # low = unusually deep for this ETF
        "dd_z": dd / vol60 if vol60 else np.nan,
        "vs_sma200": last / sma200 - 1,
        "vs_sma50": last / sma50 - 1,
        "rs_spy_3m": ret(px, 63) - ret(spy, 63),
        "rs_spy_6m": ret(px, 126) - ret(spy, 126),
        "rs_spy_12m": ret(px, 252) - ret(spy, 252),
        "ret_10d": ret(px, 10),
        "vol_60d": vol60,
        "dollar_vol": (px * vol).iloc[-20:].mean(),
        "tp_pct": tp,
        "sl_pct": sl,
        "dip_low_pct": dip_low / last - 1,   # informational: structural stop; 0 = sitting on the low
        "rr": tp / -sl if sl else np.nan,
        "size_1pct": RISK / -sl if sl else np.nan,
    }


def flag_dips(df):
    """Adds is_dip, stabilizing, dip_score (0 = most beaten up). Returns sorted df."""
    df = df.copy()
    deep = (df.vs_sma200 < 0) | (df.dd_52w <= DD_MIN)
    df["is_dip"] = deep & (df.rs_spy_3m < 0)
    df["stabilizing"] = df.ret_10d > 0
    dips = df[df.is_dip]
    df["dip_score"] = dips[["dd_z", "rs_spy_6m", "vs_sma200"]].rank(pct=True).mean(axis=1)
    df["theme_score"] = df.dip_score.groupby(df.theme).transform("min").where(df.is_dip)   # theme's best dip
    df["is_candidate"] = df.is_dip & (df.theme_score.rank(method="dense") <= TOP_THEMES)
    return df.sort_values(["is_candidate", "theme_score", "dip_score", "rs_spy_3m"], ascending=[False, True, True, True])


def main():
    tickers = list(THEME)
    raw = yf.download(tickers, period="3y", auto_adjust=True, progress=False, threads=True)
    close, volume = raw["Close"], raw["Volume"]
    now = pd.Timestamp.now(tz="America/New_York")
    if close.index[-1].date() == now.date() and now.hour < 16:   # drop today's partial bar
        close, volume = close.iloc[:-1], volume.iloc[:-1]
    asof = close.index[-1].date()
    spy = close[BENCH]
    rows = {}
    for t in tickers:
        if t not in close or close[t].dropna().shape[0] < 30:
            print(f"skip {t}: no data", file=sys.stderr)
            continue
        rows[t] = metrics(close[t], volume[t], spy)
    df = pd.DataFrame(rows).T
    df.insert(0, "theme", pd.Series(THEME))
    df.insert(1, "asof", str(asof))
    liquid = df.dollar_vol >= MIN_DOLLAR_VOL          # NaN volume counts as illiquid
    if (~liquid).any():
        print(f"dropped illiquid: {' '.join(df.index[~liquid])}", file=sys.stderr)
    df = flag_dips(df[liquid])
    young = df.index[df.rs_spy_3m.isna()]
    if len(young):
        print(f"too young for rs_spy_3m (cannot flag): {' '.join(young)}", file=sys.stderr)
    OUT.parent.mkdir(exist_ok=True)
    df.to_csv(OUT, float_format="%.4f")

    cols = ["theme", "dd_52w", "dd_z", "dd_pctile", "vs_sma200", "rs_spy_3m", "rs_spy_6m", "ret_10d", "stabilizing", "dip_score"]
    pd.set_option("display.width", 200)
    c = df[df.is_candidate]
    print(f"\n=== CANDIDATES: {len(c)} dips in the top {c.theme.nunique()} themes ({df.is_dip.sum()} dips of {len(df)}) as of {asof} ===")
    print(c[cols].to_string(float_format="{:.3f}".format))
    rest = df[df.is_dip & ~df.is_candidate]
    if len(rest):
        print(f"\nother dips (themes ranked > {TOP_THEMES}): {' '.join(rest.index)}")
    print("\n=== LEADERS (rs_spy_3m) — regime ===")
    print(df.sort_values("rs_spy_3m", ascending=False)[["theme", "rs_spy_3m", "rs_spy_6m", "dd_52w"]].head(8).to_string(float_format="{:.3f}".format))
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
