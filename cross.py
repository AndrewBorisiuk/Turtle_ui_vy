from random import randint
from turtle import *
speed(0)

def draw_cross(x, y, col):
    size = 60
    start(x, y)
    color(col); width(10); setheading(45)
    fd(1.4 * size)
    start(x + size, y)
    setheading(135)
    fd(1.4 * size)

def draw_dot(x, y, col):
    size = 60
    start(x + size // 2, y)
    color(col); setheading(0)
    circle(size // 2)


def start(x, y):
    penup(); goto(x, y); pendown()

def square(size, w, col):
    width(w); fillcolor(col); begin_fill()
    for _ in range(4):
        fd(size); rt(90)
    end_fill()

x_start,y_start = -150,150
size = 100

def draw_field():
  #твій код
    x,y = x_start, y_start
    for i in range(3):
        for j in range(3):
            start(x, y)
            square(size, 3, "white")
            x+=size
        x = x_start
        y -= size

#ігрове поле
playing_field = [None, -1,-1,-1,-1,-1,-1,-1,-1,-1]
#координати клітинок ігрового поля
x_cor = [None, -150,-50,50,-150,-50,50,-150,-50,50]
y_cor = [None, 50,50,50,-50,-50,-50,-150,-150,-150]
#розмір клітинок ігрового поля
size = 100

winner = False

def move_player(player,col):
    global winner
    while True:
        cell = int(input("Введіть номер клітинки від 1 до 9"))
        if playing_field[cell]!=-1:
            print("Клітинки вже зайнята!")
            continue
        playing_field[cell] = player
        if player == 1:
            draw_cross(x_cor[cell], y_cor[cell], col)
        else:
            draw_dot(x_cor[cell], y_cor[cell], col)
        break
        # if playing_field[1] == playing_field[2] == playing_field[3]:
        #     if playing_field[1] == 1:
        #         print("X гравець переміг")
        #     elif playing_field[1] == 0:
        #         print("0 гравець переміг")
        #     winner = True
        #     break


def check_win():
    if playing_field[1] == playing_field[2] == playing_field[3]: return playing_field[1]
    if playing_field[4] == playing_field[5] == playing_field[6]: return playing_field[4]
    if playing_field[7] == playing_field[8] == playing_field[9]: return playing_field[7]
    if playing_field[1] == playing_field[4] == playing_field[7]: return playing_field[1]
    if playing_field[2] == playing_field[5] == playing_field[8]: return playing_field[2]
    if playing_field[3] == playing_field[6] == playing_field[9]: return playing_field[3]
    if playing_field[1] == playing_field[5] == playing_field[9]: return playing_field[1]
    if playing_field[3] == playing_field[5] == playing_field[7]: return playing_field[3]
 
draw_field()
player = randint(0, 1)
 
while True:
    if player == 1:
        move_player(1, 'red')
        player = 0
    else:
        move_player(0, 'blue')
        player = 1
 
    win = check_win()
    if win == 1:
        print("Виграв Хрестики!")
        break
    if win == 0:
        print("Виграв Нулик!")
        break

print("Кінець гри")

while not winner: 
    move_player(1, 'red')
    move_player(0, 'blue')

