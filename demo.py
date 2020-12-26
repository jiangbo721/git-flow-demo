# -*- coding: utf-8 -*

import time


def fib(n):
    if n <= 2:
        res = 1
    else:
        res = fib(n - 1) + fib(n - 2)

    return res


def sum_squares(n):
    start_time = time.time()
    res = 0
    for i in range(n + 1):
        res += i ** 2
    end_time = time.time()
    duration = end_time - start_time
    print(f'计算0到{n}的平方和耗时:{duration: .4f}s, 将结果为:{res}')
    return res


class Ocr:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def process(self):
        print(f"Ocr processing {self.name}...")

    def main(self):
        pass


if __name__ == '__main__':
    sum_squares(10000)
    ocr = Ocr("test", "")
    ocr.process()
