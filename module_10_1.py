import threading
import time
class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.day = 0
        self.monsters = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.monsters > 0:
            self.monsters -= self.power
            time.sleep(1)
            self.day += 1
            print(f"{self.name} сражается {self.day} день(дня)..., осталось {max(self.monsters, 0)} воинов.\n")
        print(f"{self.name} одержал победу спустя {self.day} дней(дня)!\n")

first_knight = Knight('Sir Lancelot', 10)

second_knight = Knight("Sir Galahad", 20)
first_knight.start()
time.sleep(1)
second_knight.start()
first_knight.join()
second_knight.join()