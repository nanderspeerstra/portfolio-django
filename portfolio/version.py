# portfolio/version.py
from pathlib import Path


def get_version():
    version_file = Path(__file__).resolve().parent.parent / "version.txt"
    try:
        return version_file.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return "dev"
