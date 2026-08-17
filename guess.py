from turtle import *
from random import *
speed(0)

word = 'spaceship'
# Список кольорів пелюсток
colors = ["#c0392b", "#8e44ad", "#2471a3", "#138d75", "#f1c40f","#e74c3c","#5dade2"]
# координати квітки
x_start,y_start = 50,-150
# радіус пелюстки та листочків
r = 95 #по необхідності змінити
# стартовий кут для пелюсток квітки
starting_angle = 360/7

count_right = 0
count_wrong = 0

print("a" in "sasha")
print("n" in "sasha")

def draw_cross(x, y, col):
    size = 60
    start(x, y)
    color(col); width(10); setheading(45)
    fd(1.4 * size)
    start(x + size, y)
    setheading(135)
    fd(1.4 * size)
    
def draw_petal(col, radius):
    color(col)
    begin_fill()
    circle(radius, 60) 
    left(120) 
    circle(radius, 60) 
    end_fill()

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
    
def draw_petal(col, radius):
    color(col)
    begin_fill()
    circle(radius, 60) 
    left(120) 
    circle(radius, 60) 
    end_fill()

def draw_stem():
    start(x_start,y_start)
    setheading(90)
    color("green")
    width(20)
    fd(50)
    setheading(135)
    draw_petal("green",100)
    #розвернути вправо та малювати листочок
    setheading(25)
    draw_petal("green",65)
    setheading(90)
    fd(150)
    
def draw_petals():    
# Малювання квітки
    width(20)
    k = starting_angle
    start(x_start,y_start+200)
    for i in range(len(colors)):   
        setheading(k)
        draw_petal(colors[i], r)
        k += starting_angle

def draw_flower():
    draw_stem()
    draw_petals()
    
def draw_down_petal(col):
    draw_flower()
    xd = randint(x_start-50,x_start+50)
    start(xd,y_start)
    h = randint(180,360)
    setheading(h)
    width(20)
    draw_petal(col, r)
    
def end_game(col,txt):
    start(-100,150)
    color(col)
    write(txt, font=("Arila",10))

draw_flower()
while True:
    letter = input("Введіть літеру")
    if letter in word:
        count_right += 1
    else:
        col = colors[count_wrong] 
        colors[count_wrong] = "white"
        count_wrong += 1
        draw_down_petal(col)
    if count_wrong == 7:
        end_game("red",f"Ти програв :( слово було  - {word}")
        break
    elif count_right == 9:
        end_game("blue",f"Ти виграв :( слово було  - {word}")
        break