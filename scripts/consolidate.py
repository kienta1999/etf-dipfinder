"""Merge panel ballots → output/<DATE>/scores.csv. Usage: uv run python scripts/consolidate.py 2026-09-06"""
import re, sys
from pathlib import Path
import pandas as pd

W = {"cause": .30, "necessity": .20, "catalyst": .20, "basket": .15, "price": .15}
VETO = 3  # cause <= VETO → avoid

def parse(p):
    rows = re.findall(r"^\|\s*\d+\s*\|\s*([A-Z]+)\s*\|\s*(\d+)\s*\|", p.read_text(), re.M)
    return {t: int(s) for t, s in rows}

def main(date):
    out = Path(__file__).resolve().parent.parent / "output" / date
    scan = pd.read_csv(out.parent.parent / "data" / "scan.csv", index_col=0)
    df = pd.DataFrame({l: parse(out / f"score_{l}.md") for l in W if (out / f"score_{l}.md").exists()})
    have = [l for l in W if l in df]
    wsum = sum(W[l] for l in have)
    df["wtd"] = sum(df[l] * W[l] for l in have) / wsum
    df["veto"] = df.get("cause", pd.Series(10, index=df.index)) <= VETO
    df["dip_score"] = scan.dip_score.reindex(df.index)
    df["dip_rank"] = df.dip_score.rank(method="min").astype(int)
    df["stabilizing"] = scan.stabilizing.reindex(df.index)
    df = df.sort_values("wtd", ascending=False)
    df.insert(0, "wtd_rank", range(1, len(df) + 1))
    df.to_csv(out / "scores.csv", float_format="%.2f")
    print(f"lenses: {have} (weights renormalised to {wsum:.2f})")
    print(df.to_string(float_format="{:.2f}".format))

if __name__ == "__main__":
    main(sys.argv[1])
