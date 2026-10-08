from pathlib import Path
from urllib.request import urlopen
from hashlib import sha256
import json

def download_update(release,current_version):
    asset = next(
        (a for a in release['assets'] if a["name"] == "app.py"),
        None
    )

    assert asset, ValueError("this version have not app.py file")

    target = Path(__file__).resolve().parent.parent / "app.new.py"

    with urlopen(asset["browser_download_url"],timeout=30) as response:
        data = response.read()


    
    expected = asset.get('digest')
    actual = "sha256:" + sha256(data).hexdigest()
    assert expected, ValueError("request have not data checksum")
    assert expected == actual, ValueError("checksum failed, please retry it")

    target.write_bytes(data)
    metadata = {
        "from_version":current_version,-
        "to_version":release['tag_name'],
        "digest":expected
    }

    target.with_suffix(".json").write_text(
        json.dumps(metadata,indent=2),
        encoding='utf-8'
    )
    
    print("checksum pass and download file done")
    return target

