import subprocess 
import sys

from pathlib import Path

from update.install import validate_update,install_update

APPDIR = Path(__file__).resolve().parent

while True:
    result = subprocess.run(
        [sys.executable,str(APPDIR / "app.py")],
        cwd=APPDIR
    )

    if result.returncode != 75:
        print(f"应用已退出，exit code :{result.returncode}")
        break

    try:
        validate_update()
        backup = install_update()

    except Exception as e:
        print(f"应用更新失败：{e}")
        break

    print(f"文件已替换，备份：{backup}")
    print("正在重新启动应用")