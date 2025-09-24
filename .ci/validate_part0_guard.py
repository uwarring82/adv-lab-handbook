import os, sys
BLOCKED_DIR = os.path.join("handbook","part-0-lab-alliance-compact")
# allow override with ERB token in commit message (from env or file)
commit_msg = os.environ.get("GIT_COMMIT_MSG","")
if "[ERB-APPROVED]" in commit_msg:
    sys.exit(0)
changed = os.popen("git diff --name-only origin/main...HEAD").read().strip().splitlines()
if any(p.startswith(BLOCKED_DIR) for p in changed):
    print("Part 0 changes require ERB approval token [ERB-APPROVED].")
    sys.exit(1)
