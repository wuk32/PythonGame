# coding=utf8
import pgzrun
import random

WIDTH=800
HEIGHT=600
x=WIDTH//2
y=HEIGHT//2
speed_x = 3
speed_y = 5
r = 30
colorR = 255
colorG = 0
colorB = 0

balls = []
def generate_ball(num):
    for i in range(num):
        x = random.randint(100, WIDTH-100)
        y = random.randint(100, HEIGHT-100)
        r = random.randint(5, 50)
        speed_x = random.randint(1, 5)
        speed_y = random.randint(1, 5)
        colorR = random.randint(0, 255)
        colorG = random.randint(0, 255)
        colorB = random.randint(0, 255)
        balls.append([x, y, speed_x, speed_y, r, colorR, colorG, colorB])

def draw():
    screen.fill('white')
    for ball in balls:
        screen.draw.filled_circle((ball[0], ball[1]), ball[4], (ball[5], ball[6], ball[7]))

def update():
    for ball in balls:
        ball[0] += ball[2]
        ball[1] += ball[3]
        if ball[0] >= WIDTH - ball[4] or ball[0] <= ball[4]:
            ball[2] *= -1
        if ball[1] >= HEIGHT - ball[4] or ball[1] <= ball[4]:
            ball[3] *= -1  

def on_mouse_move(pos, rel, buttons):
    if mouse.LEFT in buttons:
        generate_ball(1)

pgzrun.go()
