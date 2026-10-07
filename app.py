import datetime
__VERSION__ = '1.1.0'

print(f"v{__VERSION__:}")
print("hello world")

def read_date_time():
    date = datetime.date.today()
    print(f"today is {date}")

read_date_time()

input("press Enter to Exit")
