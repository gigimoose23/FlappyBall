import pygame
import pgzero
import pgzrun
import random
GRAVITY = 300
TITLE = "Flappy Ball"
red = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
blue = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
green = (random.randint(1,255),random.randint(1,255),random.randint(1,255))


class TheBall:
    def __init__(self, start_x, start_y, radius):
        self.radius = radius
        self.start_x = start_x
        self.start_y = start_y

        self.vx = 100
        self.vy = 0

    def draw(self):
        pos = (self.start_x, self.start_y)
        screen.draw.filled_circle(pos, self.radius, red)


newBall = TheBall(500,0, 70)






def update(dt):
   
    uy = newBall.vy
    newBall.vy = newBall.vy + GRAVITY * dt
    newBall.start_y =  newBall.start_y + (uy + newBall.vy) * 0.5 * dt
    if newBall.start_y > screen.height - newBall.radius:
        newBall.start_y = screen.height - newBall.radius
        newBall.vy = -newBall.vy * 0.9
    newBall.start_x = newBall.start_x + newBall.vx * dt
    if newBall.start_x > screen.width - newBall.radius or newBall.start_x < newBall.radius:
        newBall.vx = -newBall.vx


def on_key_down(key):
    if key == keys.SPACE:
        newBall.vy = -500



def draw():
    screen.clear()
    newBall.draw()




pgzrun.go()