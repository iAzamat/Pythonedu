import datetime
import time


def exp_txt(data):
    with open(f'./log/log.txt', 'a', encoding='utf-8') as f:
        date = round(time.time() * 1000)
        date2 = str(datetime.datetime.fromtimestamp(date / 1000.0)).split('.')[0]
        f.write(f'[{date2}] {data}\n')
