import datetime
from update import check_for_updates
from update.download import download_update
__VERSION__ = '1.3.0'

print(f"v{__VERSION__:}")
print("hello world")

def read_date_time():
    date = datetime.date.today()
    print(f"today is {date}")

read_date_time()
print(f"当前时间：{datetime.datetime.now():%H:%M:%S}")

try:
    release = check_for_updates(__VERSION__)

    if release is None:
        print("没有可用更新")
    else:
        answer = input(f"发现可用更新{release['tag_name']} ，是否下载？[y/n]")

        if answer.strip().lower() == "y":
            path = download_update(release,__VERSION__)
            print(f"已下载并校验，等待安装：{path.name}")
            raise SystemExit(75)
        else:
            print("已经暂停下载")
except Exception as error:
    print(f"更新检查或下载失败，继续运行：{error}")

input("press Enter to Exit")

