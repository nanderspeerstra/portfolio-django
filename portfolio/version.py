import json
from pathlib import Path


def get_version():
    manifest_file = (
        Path(__file__).resolve().parent.parent
        / ".release-please-manifest.json"
    )
    try:
        data = json.loads(manifest_file.read_text(encoding="utf-8"))
        return data.get(".", "dev")
    except FileNotFoundError:
        return "dev"
