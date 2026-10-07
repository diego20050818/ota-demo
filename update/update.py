import json
from urllib.request import urlopen

RELEASE_URL = "https://api.github.com/repos/diego20050818/ota-demo/releases/latest"

def get_latest_release():
    """get github latest app version info
    """
    with urlopen(RELEASE_URL,timeout=10) as response:
        return json.load(response)