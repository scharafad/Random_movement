#!/usr/bin/python
# coding=utf-8
import pgzrun
import random  # подключение библиотеки рандомных чисел  
alien = Actor('alien')  # Загрузка спрайта героя
speed = random.randint(1, 3)  # Установка скорости
WIDTH = 500  # Ширна рабочего окна
HEIGHT = 500  # Высота рабочего окна
step = 10  # Кол-во шагов в выбранную сторону
choose = 1  # Выбор направления
def draw():  # Функция отрисовки экрана и героя
    screen.clear()  
    alien.draw()  
def update():  
    global step, choose  
    if step == 10:  # Обнуление направления
        choose = random.randint(1, 4)
        step = 0
    if choose == 1:  # Направление 1 (вправо)
        alien.left += speed
    elif choose == 2:  # Направление 2 (влево)
        alien.left -= speed
    elif choose == 3:  # Направление 3 (вверх)
        alien.top -= speed
    else:  # Нарпавление 4 (вниз)
        alien.top += speed    
    if alien.left > WIDTH - alien.width:  # Ограничение движения справа
        alien.left -= speed  
    elif alien.left < 0:  # Ограничение движения слева
        alien.left += speed
    elif alien.top < 0:  # Ограничение движения сверху
        alien.top += speed 
    elif alien.top > HEIGHT - alien.height:  # Ограничение движения снизу
        alien.top -= speed  
    step += 1  # увеличить шаг
alien.center = 250, 250  # начальное положение
pgzrun.go()
