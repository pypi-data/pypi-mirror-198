import time
from functools import wraps


def cost(fn):
    @wraps(fn)
    def wrap():
        start = int(time.time())
        fn()
        end = int(time.time())
        print(f'函数 {fn.__name__} 执行花费时间：{end-start} 秒')
    return wrap
