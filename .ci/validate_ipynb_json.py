import json, sys, glob
bad = []
for nb in glob.glob("**/*.ipynb", recursive=True):
    try:
        with open(nb, "r", encoding="utf-8") as f:
            json.load(f)
    except Exception as e:
        bad.append(f"{nb}: {e}")
if bad:
    print("Invalid notebooks (not valid JSON):")
    print("\n".join("  - "+x for x in bad))
    sys.exit(1)
