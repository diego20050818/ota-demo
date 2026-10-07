from .update import get_latest_release
def version_tuple(version:str) -> tuple:
    """将 vx.x.x的格式转换为逐数字元组

    Args:
        version (str): 版本数字，格式vx.x.x

    Returns:
        tuple: 返回(x,x,x)
    """
    return tuple(map(int,version.removeprefix("v").split(".")))

def check_for_updates(current_version):
    """检查更新，release page的latest是否比目前大

    Args:
        current_version (str): 版本号 格式vx.x.x

    Returns:
        None | tuple: 如果不需要更新，则返回None ，如果需要更新，返回目标版本号
    """
    release = get_latest_release()

    if version_tuple(release["tag_name"]) > version_tuple(current_version):
        return release

    return None

if __name__ == '__main__':
    from update import get_latest_release
    cur = 'v1.1.0'
    print(check_for_updates(cur))