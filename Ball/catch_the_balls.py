

import pygame
from pygame.draw import *
from random import randint
from math import pi, sin, cos
import csv
from time import asctime

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
screen_width, screen_height = 1200, 800


def main():
    global balls, username
    """
    определяем цикл обработки србытий
    """
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))

    FPS = 30
    score = 0
    username = ""
    cycle = 5.5

    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        balls = ballslist(6, 55, 3)
        start_time = time(pygame.time.get_ticks(), 0, cycle)
        present_time = 0
        while (present_time - start_time) / 1000 < cycle:
            present_time = pygame.time.get_ticks()
            balls_move(screen)
            bounce(balls)
            show_score(screen, score)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    while not finished:
                        menu(screen, score)
                        finished = users_typing(screen, score)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    score = ranking(score)
            pygame.display.update()
            screen.fill(BLACK)

    pygame.quit()


def ballslist(number, size, v=3):
    """
    создаем список 
    param number: кол-во obj
    size: размер объектов
    V: скорость
    возвращаем список объектов
    """
    param = []
    for i in range(number):
        angle = randint(0, int(2 * pi * 100))
        param.append({
            'x': randint(100, screen_width - 100),
            'y': randint(100, screen_height - 100),
            'Vx': v * cos(angle / 100),
            'Vy': v * sin(angle / 100),
            'r': randint(40, 255),
            'g': randint(40, 255),
            'b': randint(40, 255),
            's': size
        })
    return param

def balls_move(surface):
    """
    передвигаем шарики

    """
    for obj in balls:
        ellipse(surface, (obj['r'], obj['g'], obj['b']),
                (obj['x'] - obj['s'], obj['y'] - obj['s'], 2 * obj['s'], 2 * obj['s']))
        obj['x'] += obj['Vx']
        obj['y'] += obj['Vy']




def bounce(param):
    """
    меняем скорость шариков после столкновения со стенкой
 
    """
    for obj in param:
        if obj['x'] - obj['s'] <= 0:
            obj['Vx'] = abs(obj['Vx'])
        if obj['y'] - obj['s'] <= 0:
            obj['Vy'] = abs(obj['Vy'])
        if obj['x'] + obj['s'] >= screen_width:
            obj['Vx'] = -abs(obj['Vx'])
        if obj['y'] + obj['s'] >= screen_height:
            obj['Vy'] = -abs(obj['Vy'])


def show_score(surface, score):
    """
    показывает очки игрока в углу экрана
    
    """
    font = pygame.font.SysFont('arial', 25, True)
    text_1 = font.render("Score : {}".format(score), True, RED)
    surface.blit(text_1, (0, 0))


def menu(surface, score):
    """
    показывет меню с очками игрока
 
    """
    surface.fill(BLACK)
    font = pygame.font.SysFont('arial', 32, True)
    text_1 = font.render("Your score is {}".format(score), True, RED)
    text_2 = font.render("Please enter your name(Enter) and press F1 to quit", True, RED)
    surface.blit(text_1, text_1.get_rect(center=(screen_width / 2, screen_height / 3)))
    surface.blit(text_2, text_2.get_rect(center=(screen_width / 2, screen_height * 2 / 3)))


def users_typing(surface, score):
    """
    игрок пишет свой username и его score сохраняется в файл Players_Scores

    """
    
    global username
    font = pygame.font.SysFont('arial', 32, True)
    text_1 = font.render(username, True, RED)
    surface.blit(text_1, text_1.get_rect(center=(screen_width / 2, screen_height / 2)))
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_BACKSPACE:
                username = username[:-1]
            elif events.key == pygame.K_ESCAPE:
                return True
            elif events.key == pygame.K_F1:
                if username != "":
                    with open('Players_Scores.csv', 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow([username, score, asctime()])
                return True
            else:
                username += events.unicode


def ranking(score):
    """
    проверяем клик на obj 
 
    """
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for obj in balls:
        if (mouse_x - obj['x']) ** 2 + (mouse_y - obj['y']) ** 2 <= obj['s'] ** 2:
            score += 1
            obj['x'], obj['y'] = 2 * screen_width, 2 * screen_height
            obj['Vx'], obj['Vy'] = 0, 0
   
    return score


def time(present_t, start_t, cycle):
    """
    вычисляет время через которое начнется новый cycle

    """
    if present_t - start_t >= cycle:
        start_t = present_t
    return start_t


if __name__ == '__main__':
    main()