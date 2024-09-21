from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name: str, power: int):
        self.kname = name
        self.power = power
        super().__init__()

#При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
# Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# По прошествию 1 дня сражения (1 секунды) выводится строка
# "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
# После победы над всеми врагами выводится надпись
# "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
    def run(self):
        print(f'{self.kname} на нас напали!')
        enemy = 100
        days = 0
        while enemy > 0:
            sleep(1)
            days += 1
            enemy -= self.power
            if enemy < 0:
                enemy = 0
            print(f'{self.kname} сражается {days} суток, осталось {enemy} воинов врага.')
        print(f'{self.kname} одержал победу спустя {days} дней(я)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы окончены')

# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения
