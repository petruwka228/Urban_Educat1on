import time
from multiprocessing import Pool
import os


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            s = f.readline()
            if not s:
                break
            all_data.append(s)
if __name__ == '__main__':
    t1 = time.time()
    filenames = [f'file {number}.txt' for number in range(1, 5)]
    for i in filenames:
        read_info(i)
    t2 = time.time()
    print(t2 - t1, '(линейный)')
    with Pool() as pool:

    t1 = time.time()
        pool.map(read_info, filenames)
    t2 = time.time()

    print(t2 - t1, '(многопроцессный)')