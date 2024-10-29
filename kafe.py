from threading import Thread
import queue
import random
import time


class Table:  # класс столов
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):  # потоковый класс гостей
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(2, 10))  # генератор расторопности гостя


class Cafe:  # класс кафе
    def __init__(self, *tables):
        self.tables = tables
        self.q = queue.Queue()  # создание объекта класса очередь
        self.t_cnt = 0  # счётчик занятых столов

    def guest_arrival(self, *guests):  # метод прибытия гостей
        for g in guests:  # перебор гостей
            g_set = 0  # флаг посадки гостя
            for t in self.tables:  # перебор столов
                if t.guest == None:  # проверка занятости стола
                    t.guest = g  # присваиваем параметру гостя за столом в качестве значения поток этого гостя
                    g_set = 1  # взведение флага посадки гостя
                    print(f'{g.name} сел за стол номер {t.number}.')
                    self.t_cnt += 1
                    break  # выход из перебора столов
            if g_set == 1:  # проверка на посадку гостя
                g.start()  # запуск потока посаженного гостя
                continue  # переход к следующему гостю
            else:
                self.q.put(g)  # помещение гостя в очередь
                print(f'{g.name} в очереди.')

    def discuss_quests(self):  # метод обслуживания гостей
        while self.t_cnt > 0 or not self.q.empty():  # цикл обслуживания
            for tb in self.tables:  # перебор столов
                if tb.guest == None:  # проверка на занятость стола
                    continue  # переход к следующему столу
                elif tb.guest.is_alive():  # проверка клиентов на сытость )))
                    continue  # переход к следующему столу
                else:
                    print(f'{tb.guest.name} покушал(-а) и ушёл(ушла) из-за стола номер {str(tb.number)}.')
                    if not self.q.empty():  # проверка очереди на пустоту
                        tb.guest = self.q.get()  # садим за освободившийся стол человека из очереди
                        print(f'{tb.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {str(tb.number)}')
                        tb.guest.start()  # запуск потока посаженного гостя
                    else:
                        tb.guest = None  # обнуление стола
                        self.t_cnt -= 1
                        print(f'Стол номер {str(tb.number)} освободился.')
        print('Все гости обслужены')


# TEST ----------------------------------------------------------------------------------------------------------------

tables = [Table(number) for number in range(1, 6)]  # список столов, состоящий из объектов класса Table

guests_names = ['Oleg', 'Masha', 'Sasha', 'Vera', 'Igor', 'Lex', 'Rex', 'Lis', 'Tan', 'Han', 'Dzen',
                'Finch']  # список имён

guests = [Guest(name) for name in guests_names]  # список гостей, состоящий из объектов класса Guest

cf = Cafe(*tables)  # объект класса Cafe, заполненный столами

cf.guest_arrival(*guests)  # приём гостей

cf.discuss_quests()  # обслуживание гостей
