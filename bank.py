import time
import threading

#lock1 = Lock()

class Bank:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self):
        for i in range(10):
            self.balance = self.balance + 10
            print(f'Пополнение: {'10'}. Баланс: {str(self.balance)}')
            time.sleep(0.1)
    def take(self):
        for i in range(10):
            a = 20
            print(f'Запрос на: {str(a)}.')
            if a <= self.balance:
                self.balance = self.balance - a
                print(f'Снятие: {str(a)}')
                time.sleep(0.1)
            else:
                print('Запрос отклонён, недостаточно средств.')
                time.sleep(0.1)

# TEST ----------------------------------------------------------------------------------------------------------------

bnk = Bank(100)

dep = threading.Thread(target=bnk.deposit(), args=())
tak = threading.Thread(target=bnk.take(), args=())

#dep.start()
#tak.start()
#dep.join()
#tak.join()

#bnk.take()