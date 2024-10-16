import threading
import time


def write_words(word_count, file_name):  # определение функции
    a = open(file_name, 'w', encoding='utf-8')  # открытие файла на перезапись
    for i in range(word_count):
        a.write(f'Какое-то слово № {str(i + 1)} \n')
        time.sleep(0.1)  # задержка
    a.close()  # закрытие файла
    print('Завершилась запись в файл ' + file_name)


a1 = threading.Thread(target=write_words, args=(10, 'ww11.txt'))  # инициализация потока
a2 = threading.Thread(target=write_words, args=(30, 'ww12.txt'))
a3 = threading.Thread(target=write_words, args=(200, 'ww13.txt'))
a4 = threading.Thread(target=write_words, args=(100, 'ww14.txt'))

# TEST ----------------------------------------------------------------------------------------------------------------

"""Запуск нескольких функций с замером времени выполнения"""

ft_start = time.time()
write_words(10, 'ww1.txt')
write_words(30, 'ww2.txt')
write_words(200, 'ww3.txt')
write_words(100, 'ww4.txt')
ft_stop = time.time()
print('Работа функций ' + str(ft_stop - ft_start))

"""Запуск нескольких потоков с замером времени выполнения"""

fp_start = time.time()
a1.start()
a2.start()
a3.start()
a4.start()
a1.join()
a2.join()
a3.join()
a4.join()
fp_stop = time.time()
print('Работа потоков ' + str(fp_stop - fp_start))
