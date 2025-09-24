import json, sys, glob
bad = []
for nb in glob.glob("notebooks/**/*.ipynb", recursive=True) + glob.glob("notebooks/*.ipynb"):
    with open(nb, "r", encoding="utf-8") as f:
        data = json.load(f)
    cells = data.get("cells", [])
    if not cells: bad.append(nb); continue
    c0 = cells[0]
    ok_md = c0.get("cell_type")=="markdown"
    src = "".join(c0.get("source", []))
    meta = c0.get("metadata", {})
    ok_text = "Ethical Reminder" in src
    ok_lock = (meta.get("editable")==False and meta.get("deletable") == False)
    if not (ok_md and ok_text and ok_lock):
        bad.append(nb)
if bad:
    print("Notebooks missing immutable Ethical Reminder header:", *bad, sep="\n  - ")
    sys.exit(1)
