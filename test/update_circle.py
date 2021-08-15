# coding=utf8

import pgzrun

r = 100
def draw():
    # screen.draw.circle((400, 300), 100, "white")
    screen.fill('white')
    screen.draw.filled_circle((150, 300), r, "red")

def update():
    global r
    r = r + 1


pgzrun.go()