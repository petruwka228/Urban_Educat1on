import threading
import time
def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(word_count):
            f.write(f"Какое-то слово № {i}" )
            time.sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")
time_start = time.time()
a = write_words(10, 'example1.txt')
b = write_words(30, 'example2.txt')
c = write_words(200, 'example3.txt')
d = write_words(100, 'example4.txt')
time_end = time.time()
print(f'Работа потоков {time_end - time_start}')
threads = [
    (threading.Thread(target=write_words, args=(10, 'example5.txt'))),
    (threading.Thread(target=write_words, args=(30, 'example6.txt'))),
    (threading.Thread(target=write_words, args=(200, 'example7.txt'))),
    (threading.Thread(target=write_words, args=(100, 'example8.txt')))
]
time_start = time.time()
for i in threads:
    i.start()
for i in threads:
    i.join()
time_end = time.time()
print(f'Работа потоков {time_end - time_start}')