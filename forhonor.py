from threading import Thread
import time

class Knight(Thread):  # определение потокового класса
    def __init__(self, name, power):  # инициализация объекта класса
        super().__init__()
        self.name = name  # имя (str)
        self.power = power  # сила (int)

    def run(self):  # основная функция
        vr = 100 # исходное количество врагов
        dc = 0  # счётчик дней
        print(f'{self.name}, на нас напали!')
        while vr > 0:
            dc += 1  # инкремент счётчика дней битвы
            vr = vr - self.power  # схватка за 1 день
            if vr <= 0:  # проверка остатков
                break
            else:
                print(f'Рыцарь {self.name} сражается {str(dc)} дней(дня), осталось {str(vr)} врагов.')
                time.sleep(1)
        print(f'Рыцарь {self.name} одержал победу за {str(dc)} дней(дня)')


# TEST ----------------------------------------------------------------------------------------------------------------

r1 = Knight('Игорь', 10)  # инициализация потока
r2 = Knight('Саня', 20)

r1.start()  # запуск потока
r2.start()
r1.join()  # ожидание окончания выполнения потока
r2.join()
