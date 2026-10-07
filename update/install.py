import shutil
import json

from pathlib import Path
from update import version_tuple
from hashlib import sha256


def validate_update():
    app_dir = Path(__file__).resolve().parent.parent
    metadata_path = app_dir / "app.new.json"
    metadata = json.loads(metadata_path.read_text(encoding='utf-8'))

    candidate = app_dir / "app.new.py"
    actual = "sha256:" + sha256(candidate.read_bytes()).hexdigest()
    if actual != metadata['digest']:
        raise ValueError("sumcheck failed")

    print("checksum pass")
    current = version_tuple(metadata['from_version'])
    target = version_tuple(metadata['to_version'])

    if target <= current:
        raise ValueError("target lower than current version")

    return metadata

def install_update():
    app_dir = Path(__file__).resolve().parent.parent
    current = app_dir / "app.py"
    candidate = app_dir / "app.new.py"
    backup = app_dir / "app.backup.py"

    if not current.is_file() or not candidate.is_file():
        raise FileNotFoundError("缺少app.py 或app.new.py")

    shutil.copy2(current,backup)
    candidate.replace(current)
    return backup

