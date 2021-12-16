#DM me if you need explanation about the code

import pygame
import keyboard
from perlin_noise import PerlinNoise
import time
noisex = PerlinNoise(octaves=4, seed=4)
noisey = PerlinNoise(octaves=4, seed=18)

import math
import random

pygame.display.init()
screen = pygame.display.set_mode([1200, 700], pygame.RESIZABLE)

canvas_w = 1600
canvas_h = 800

class particle():
    def __init__(self):
        self.x = random.randint(0, canvas_w)
        self.y = random.randint(0, canvas_h)
        self.xv = 0
        self.yv = 0
        self.l = 0

    def update(self):
        if ((self.l > 50) or (self.x%canvas_w != self.x) or (self.y%canvas_h != self.y)):
            self.x = random.randint(0, canvas_w)
            self.y = random.randint(0, canvas_h)
            self.l = 0

        self.l += 1
        self.x += self.xv
        self.y += self.yv

        self.xv = noisex([self.x / 1000, self.y / 1000])*8
        self.yv = noisey([self.x / 1000, self.y / 1000])*8

        r = min(round(1/ ((self.x/500-80/400)**2 + (self.y/400-50/500)**2) *255), 255)
        g = min(round(1/ ((self.x/400-650/400)**2 + (self.y/240-610/240)**2) *255), 255)
        b = min(round(1/ ((self.x/550-1400/550)**2 + (self.y/450-501/450)**2) *255), 255)


        pygame.draw.line(screen, (r,g,b), (round(self.x - self.xv), round(self.y - self.yv)), (round(self.x), round(self.y)), 3)


particles = []

for i in range (80):
    particles.append(particle())


black_screen = screen.copy()
black_screen.fill((0,0,0))
black_screen.set_alpha(1)

for i in range (1):
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            screen_size = screen.get_size()
            screen.fill((0,0,0))
            pygame.display.update()


n = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            screen_size = screen.get_size()

        if keyboard.is_pressed("SPACE"):
            n += 1
            screen.fill((0,0,0))
            particles = []
            for i in range(40):
                particles.append(particle())
            noisex = PerlinNoise(octaves=3, seed=4+n)
            noisey = PerlinNoise(octaves=3, seed=64+n)

    for p in particles:
        p.update()
    pygame.display.update()
