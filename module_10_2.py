import threading
import random
import time

class Bank(threading.Thread):
    lock = threading.Lock()
    balance = 0

    def __init__(self, balance):
        super().__init__()
        self.balance = balance

    def deposit(self):
        for i in range(100):
            a = random.randint(50, 500)
            self.balance += a
            print(f"Пополнение: {a}. Баланс: {self.balance}")
            time.sleep(0.001)
            if self.balance >= 500 and Bank.lock.locked():
                Bank.lock.release()
        Bank.balance = self.balance


    def take(self):
        for i in range(100):
            a = random.randint(50, 500)
            print(f"Запрос на {a}")
            if a <= self.balance:
                self.balance -= a
                print(f"Снятие: {a}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                Bank.lock.acquire()
            time.sleep(0.001)
        Bank.balance = self.balance


# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank

th1 = threading.Thread(target=Bank.deposit, args=(Bank,))

th2 = threading.Thread(target=Bank.take, args=(Bank,))



th1.start()

th2.start()

th1.join()

th2.join()



print(f'Итоговый баланс: {Bank.balance}')