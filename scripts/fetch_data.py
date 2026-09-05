"""
Download the Chennai open datasets this project depends on into data/raw/.

Everything comes from OpenCity's CKAN portal. We resolve resource URLs through the
CKAN API rather than hard-coding UUIDs, because those change when a file is
re-uploaded.

Run from the project root:
    python scripts/fetch_data.py            # list what would be downloaded
    python scripts/fetch_data.py --download # actually download

Nothing here is edited afterwards. data/raw is immutable: every derived file is
produced by a script in src/ and written to data/interim or data/processed.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen, Request

CKAN = "https://data.opencity.in/api/3/action/package_show?id={slug}"

# slug -> (folder under data/, one-line why we need it)
DATASETS = {
    "chennai-stormwater-drain-swd-maps": (
        "raw/swd",
        "Greater Chennai Corporation drain alignments. The citywide KML is the real "
        "geometry our drainage graph is built from; the per-ward PDFs carry drain "
        "size hints. Public domain.",
    ),
    "chennai-flooding-data": (
        "ground_truth",
        "2015 flood points, inundation points with depth in INCHES, and hazard zones "
        "by return period. This is how we score the model — not a news clipping.",
    ),
    "gcc-ward-information": (
        "raw/wards",
        "Ward and zone boundaries, used to clip everything to a single ward.",
    ),
}

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "SIH26085-flood-nowcasting/0.1 (student project)"}


def resource_list(slug: str) -> list[dict]:
    req = Request(CKAN.format(slug=slug), headers=UA)
    with urlopen(req, timeout=60) as r:
        payload = json.load(r)
    if not payload.get("success"):
        raise RuntimeError(f"CKAN returned success=false for {slug}")
    return payload["result"]["resources"]


def filename_for(res: dict) -> str:
    """CKAN download URLs end in a UUID. Use the human name so the folder is readable."""
    stem = "".join(c if c.isalnum() or c in "-_" else "_" for c in res.get("name", "resource"))
    ext = (res.get("format") or Path(urlparse(res["url"]).path).suffix.lstrip(".") or "bin").lower()
    return f"{stem}.{ext}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--download", action="store_true", help="actually fetch the files")
    ap.add_argument("--only", help="limit to one dataset slug")
    args = ap.parse_args()

    total = 0
    for slug, (subdir, why) in DATASETS.items():
        if args.only and args.only != slug:
            continue
        print(f"\n=== {slug}\n    {why}")
        try:
            resources = resource_list(slug)
        except Exception as exc:  # noqa: BLE001 - we want the reason, plainly
            print(f"    COULD NOT REACH THE PORTAL: {exc}")
            print("    If this says 403 or 'tunnel failed', you are on a network that")
            print("    blocks it. Run this from your own machine, not a sandbox.")
            return 1

        dest = ROOT / "data" / subdir
        dest.mkdir(parents=True, exist_ok=True)
        for res in resources:
            name = filename_for(res)
            size = res.get("size") or "?"
            print(f"    {res.get('format','?'):5} {str(size):>10}  {name}")
            total += 1
            if not args.download:
                continue
            out = dest / name
            if out.exists():
                print(f"           already present, skipped")
                continue
            req = Request(res["url"], headers=UA)
            with urlopen(req, timeout=300) as r, out.open("wb") as fh:
                fh.write(r.read())
            print(f"           saved to {out.relative_to(ROOT)}")

    print(f"\n{total} resources listed.")
    if not args.download:
        print("Nothing was downloaded. Re-run with --download when you are ready.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
