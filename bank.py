import time
import threading
import random
from threading import Lock

lock1 = Lock()

class Bank:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self):
        for i in range(100):
            a = random.randint(50,500)
            if self.balance >= 500 and lock1.locked():
                lock1.release()  # закрытие окна блокировки
            else:
                pass
            self.balance = self.balance + a
            print(f'Пополнение: {str(a)}. Баланс: {str(self.balance)}')
            time.sleep(0.001)
    def take(self):
        for i in range(100):
            a = random.randint(50,500)
            print(f'Запрос на: {str(a)}.')
            if a <= self.balance:
                self.balance = self.balance - a
                print(f'Снятие: {str(a)}. Баланс: {str(self.balance)}')
                time.sleep(0.001)
            else:
                print('Запрос отклонён, недостаточно средств.')
                lock1.acquire()

# TEST ----------------------------------------------------------------------------------------------------------------

bnk = Bank(0)

dep = threading.Thread(target=bnk.deposit, args=())
tak = threading.Thread(target=bnk.take, args=())

dep.start()
tak.start()
dep.join()
tak.join()

print(f'Итоговый балланс: {bnk.balance}')