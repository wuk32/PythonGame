# coding=utf8

import pgzrun

def draw():
    # screen.draw.circle((400, 300), 100, "white")
    screen.fill('white')
    screen.draw.filled_circle((150, 300), 100, "red")
    screen.draw.filled_circle((400, 300), 100, "yellow")
    screen.draw.filled_circle((650, 300), 100, "blue")
pgzrun.go()