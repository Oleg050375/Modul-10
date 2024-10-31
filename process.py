from multiprocessing import Process, Pool
from time import time


def read_info(f_name):  # целевая функция
    all_data = []  # список строк
    a = open(f_name, 'r', encoding='utf-8')  # открываем файл
    b = 'start'
    while b:  # цикл построчного чтения файла до появления пустой строки
        b = a.readline()  # чтение строки из файла
        all_data.append(b)  # пополнение списка строк
    a.close()  # закрыли файл


# TEST ----------------------------------------------------------------------------------------------------------------

f_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']  # список имён файлов


def line_p(f_names_list):  # тестовая функция линейных вызовов
    f_times = []  # список длительностей чтения файлов
    for f_n in f_names_list:  # цикл чтения файлов из списка файлов
        st = time()  # запуск таймера
        read_info(f_n)  # вызов целевой функции
        ft = time()  # останов таймера
        dt = round(ft - st, 2)  # вычисление времени чтения файла
        f_times.append(dt)  # пополнение списка длительностей чтения файлов
    suma_t = sum(f_times)  # вычисление общего времени чтения всех файлов
    print(f_times, suma_t)


def proc_p_1(f_names_list):  # мультипроцессорная тестовая функция v.1
    if __name__ == '__main__':
        pr_list = [Process(target=read_info, args=(i,)) for i in f_names_list]  # формирование списка процессов
        st = time()  # запуск таймера
        for i in pr_list:  # запуск всех процессов
            i.start()
        for i in pr_list:  # запуск ожиданий окончания всех процессов
            i.join()
        ft = time()  # остановка таймера
        dt = round(ft - st, 2)  # вычисление общего времени выполнения
        print(dt)


def proc_p_2(f_names_list):  # мультипроцессорная тестовая функция v.2
    if __name__ == '__main__':
        pl = Pool()  # создание пула процессов
        st = time()  # запуск таймера
        pl.map(read_info, f_names)  # запуск мультипроцессорного метода map
        ft = time()  # останов таймера
        dt = round(ft - st, 2)  # вычисление времени чтения файла
        print(dt)


# line_p(f_names)  # запуск тестовой функции линейных вызовов

# proc_p_1(f_names)

proc_p_2(f_names)
