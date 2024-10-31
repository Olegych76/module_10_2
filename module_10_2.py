from threading import Thread
from time import sleep


class Knight(Thread):
    enemy = 100

    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def battle(self):
        days = 0
        while self.enemy > 0:
            self.enemy -= self.power
            days += 1
            print(f'{self.name} сражается {days} дней(дня), осталось {self.enemy} воинов')
            sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle()


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков
first_knight.start()
second_knight.start()
#  Остановка текущих
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')
