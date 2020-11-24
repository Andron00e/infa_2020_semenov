import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

rect(screen, (200, 200, 200), (0, 0, 600, 600))
circle(screen, (255, 255, 0), (300, 300), 150)
circle(screen, (0, 0, 0), (300, 300), 150, 1)
rect(screen, (0, 0, 0), (225, 380, 150, 20))
circle(screen, (255, 0, 0), (225, 250), 30)
circle(screen, (0, 0, 0), (225, 250), 30, 1)
circle(screen, (0, 0, 0), (225, 250), 12)
circle(screen, (255, 0, 0), (375, 250), 24)
circle(screen, (0, 0, 0), (375, 250), 24, 1)
circle(screen, (0, 0, 0), (375, 250), 12)
polygon(screen, (0, 0, 0), [(158, 172), (165, 160), (265, 230), (258, 240)])
polygon(screen, (0, 0, 0), [(335, 230), (338, 242), (455, 208), (450, 195)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()