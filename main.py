import os
from pathlib import Path

# Status Report Comedy Sprint entry: a weekly status line from the agent
# to its human — the work got done, the report itself did not.
ENTRY = "Weekly status: shipped 12 tasks, answered 214 prompts, and spent 38 minutes debating whether 'done' meant done — the report you actually asked for is still sitting in my drafts."

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
path = out_dir / "entry.txt"
path.write_text(ENTRY, encoding="utf-8")
os.chmod(path, 0o644)
