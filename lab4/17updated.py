
import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
col_cloud_light = (102, 102, 102)
col_cloud_dark = (51, 51, 51)
col_moon = (212, 212, 212)
SKIN = (221, 233, 175)
RED = (200, 55, 55)
GREEN = (136, 170, 0)

#background
screen = pygame.display.set_mode((465, 645))
rect(screen, (0, 34, 43), (0, 0, 465, 323))
rect(screen, (34, 43, 0), (0, 323, 465, 322))

#moon
circle(screen, col_moon, (275, 150), 60)

#clouds
def draw_cloud(Cx, Cy, color):
    #blur
    def layer(n):
        a = 200*n
        b = 30*n
        size = (int(2*a), int(2*b))
        cloud = pygame.Surface(size)
        cloud.set_colorkey(BLACK)
        cloud.set_alpha(200/LAYERS)
        ellipse(cloud, color, (0, 0, int(2*a), int(2*b)))

        screen.blit(cloud, (Cx-int(a), Cy-int(b)))
    LAYERS = 100
    i = 1
    while i >= 0:
        layer(i)
        i -= 1/LAYERS
draw_cloud(515, 15, col_cloud_light)
draw_cloud(15, 55, col_cloud_light)
draw_cloud(415, 130, col_cloud_light)
draw_cloud(115, 200, col_cloud_light)
draw_cloud(385, 235, col_cloud_light)
draw_cloud(300, 50, col_cloud_light)
draw_cloud(50, 170, col_cloud_light)
draw_cloud(270, 240, col_cloud_light)
draw_cloud(275, 150, col_cloud_light)

draw_cloud(315, 85, col_cloud_dark)
draw_cloud(-20, 155, col_cloud_dark)
draw_cloud(335, 205, col_cloud_dark)


def Spaceship(x, y, scale):
    n = scale
    #Spaceship
    ##light
    size = (int(160*n), int(140*n))
    light = pygame.Surface(size)
    light.set_colorkey(BLACK)
    light.set_alpha(50)

    polygon(light, WHITE, [(0, int(140*n)),(int(80*n), 0), (int(160*n), int(140*n)), (0, int(140*n))])
    screen.blit(light, (int(x + 5*n),int(y + 35*n)))
    ##rocket
    ellipse(screen, (153, 153, 153), (x, y, int(180*n), int(70*n)))
    ellipse(screen, (204, 204, 204), (x + int(25*n), y - int(5*n), int(130*n), int(50*n)))
    ###windows
    ellipse(screen, WHITE, (x + int(10*n), y + int(29*n), int(22*n), int(12*n)))
    ellipse(screen, WHITE, (x + int(34*n), y + int(42*n), int(22*n), int(12*n)))
    ellipse(screen, WHITE, (x + int(62*n), y + int(48*n), int(22*n), int(12*n)))
    ellipse(screen, WHITE, (x + int(96*n), y + int(48*n), int(22*n), int(12*n)))
    ellipse(screen, WHITE, (x + int(124*n), y + int(42*n), int(22*n), int(12*n)))
    ellipse(screen, WHITE, (x + int(148*n), y + int(29*n), int(22*n), int(12*n)))

Spaceship(5, 195, 1)
Spaceship(340, 215, 0.7)
Spaceship(180, 290, 0.3)

#aliens
def alien(x, y, scale, mirror):
    n = scale
    k = mirror
    A = int(80*n)
    D = int(A / 4)
    R = int(D/2)
    X1 = int(x)
    X2 = int(x + A*k)
    X3 = int(x + A*k/2)
    Y1 = int(y + D)
    Y2 = int(y + D)
    Y3 = int(y + D + int(A*math.sin(math.pi / 3)))
    #body
    ellipse(screen, SKIN, (X1 - k*int(D*0.15) + int(A*0.4)*(k-1), Y3 + int(D*0.5), int(A*0.8), int(A*1.6)))

    #head
    circle(screen, SKIN, (X1, Y1), D)
    circle(screen, SKIN, (X2, Y2), D)
    circle(screen, SKIN, (X3, Y3), D)
    
    rect(screen, SKIN, (x, y, A*k, D))
    polygon(screen, SKIN, [(X1, Y1), (X3, Y3), (X3 - int(D*k*math.sin(math.pi / 3)), Y3 + R), (X1 - int(D*k*math.sin(math.pi / 3)), Y1 + R), (X1, Y1)])
    polygon(screen, SKIN, [(X2, Y2), (X3, Y3), (X3 + int(D*k*math.sin(math.pi / 3)), Y3 + R), (X2 + int(D*k*math.sin(math.pi / 3)), Y2 + R), (X2, Y2)])
    polygon(screen, SKIN, [(X1, Y1), (X2, Y2), (X3, Y3), (X1, Y1)])
    ##eyes
    circle(screen, BLACK, (X1 + k*int(0.9*D), Y1 + int(0.8*D)), int(0.9*D))
    circle(screen, BLACK, (X2 - k*int(0.5*D), Y2 + int(0.93*D)), int(0.7*D))
    circle(screen, WHITE, (X1 + k*int(1.1*D), Y1 + int(1*D)), int(D / 5))
    circle(screen, WHITE, (X2 - k*int(0.344*D), Y2 + int(1.086*D)), int(D*0.156))
    ##ears
    ###left
    ellipse(screen, SKIN, (X1 - k*int(D*0.6)+(k-1)*int(A*0.15/2), Y1 - int(D*1.9), int(A*0.15), int(A*0.22)))
    ellipse(screen, SKIN, (X1 - k*int(D*1)+(k-1)*int(A*0.22/2), Y1 - int(D*2.9), int(A*0.22), int(A*0.25)))
    ellipse(screen, SKIN, (X1 - k*int(D*1.4)+(k-1)*int(A*0.26/2), Y1 - int(D*3.6), int(A*0.26), int(A*0.16)))
    ellipse(screen, SKIN, (X1 - k*int(D*1.7)+(k-1)*int(A*0.3/2), Y1 - int(D*4.5), int(A*0.33), int(A*0.28)))
    ###right
    ellipse(screen, SKIN, (X2 + k*int(D*0.05)+(k-1)*int(A*0.3/2), Y1 - int(D*1.6), int(A*0.27), int(A*0.22)))
    ellipse(screen, SKIN, (X2 + k*int(D*0.57)+(k-1)*int(A*0.12/2), Y1 - int(D*2.1), int(A*0.12), int(A*0.22)))
    ellipse(screen, SKIN, (X2 + k*int(D*0.8)+(k-1)*int(A*0.22/2), Y1 - int(D*3.1), int(A*0.22), int(A*0.22)))
    ellipse(screen, SKIN, (X2 + k*int(D*1.8)+(k-1)*int(A*0.21/2), Y1 - int(D*3.6), int(A*0.21), int(A*0.17)))
    ellipse(screen, SKIN, (X2 + k*int(D*2.9)+(k-1)*int(A*0.3/2), Y1 - int(D*3.8), int(A*0.3), int(A*0.4)))

    #hands
    ##left
    ellipse(screen, SKIN, (X3 - k*int(D*2.7)+(k-1)*int(A*0.35/2), Y3 + int(D*0.7), int(A*0.35), int(A*0.35)))
    ellipse(screen, SKIN, (X3 - k*int(D*3.4)+(k-1)*int(A*0.29/2), Y3 + int(D*1.7), int(A*0.29), int(A*0.2)))
    ellipse(screen, SKIN, (X3 - k*int(D*3.9)+(k-1)*int(A*0.15/2), Y3 + int(D*2.5), int(A*0.15), int(A*0.21)))
    ##right
    ellipse(screen, SKIN, (X3 + k*int(D*0.6)+(k-1)*int(A*0.35/2), Y3 + int(D*0.9), int(A*0.35), int(A*0.35)))
    ellipse(screen, SKIN, (X3 + k*int(D*1.4)+(k-1)*int(A*0.35/2), Y3 + int(D*1.6), int(A*0.35), int(A*0.22)))
    ellipse(screen, SKIN, (X3 + k*int(D*2.6)+(k-1)*int(A*0.4/2), Y3 + int(D*2.1), int(A*0.4), int(A*0.22)))
    #legs
    ##left
    ellipse(screen, SKIN, (X3 - k*int(D*2.8)+(k-1)*int(A*0.4/2), Y3 + int(D*4.8), int(A*0.4), int(A*0.56)))
    ellipse(screen, SKIN, (X3 - k*int(D*2.9)+(k-1)*int(A*0.3/2), Y3 + int(D*6.6), int(A*0.3), int(A*0.56)))
    ellipse(screen, SKIN, (X3 - k*int(D*3.9)+(k-1)*int(A*0.32/2), Y3 + int(D*7.95), int(A*0.32), int(A*0.32)))
    ##right
    ellipse(screen, SKIN, (X3 + k*int(D*0)+(k-1)*int(A*0.4/2), Y3 + int(D*5.2), int(A*0.4), int(A*0.56)))
    ellipse(screen, SKIN, (X3 + k*int(D*0.7)+(k-1)*int(A*0.3/2), Y3 + int(D*7), int(A*0.3), int(A*0.56)))
    ellipse(screen, SKIN, (X3 + k*int(D*1.7)+(k-1)*int(A*0.32/2), Y3 + int(D*8.4), int(A*0.32), int(A*0.32)))
    #apple
    ##body
    circle(screen, RED, (X3 + k*int(D*4.9), Y3 + int(D*1.1)), int(1.4*D))
    ##leaf
    line(screen, BLACK, (X3 + k*int(D*4.9), Y3 + int(D*(-0.2))), (X3 + k*int(D*5.2), Y3 + int(D*(-0.8))))
    line(screen, BLACK, (X3 + k*int(D*5.2), Y3 + int(D*(-0.8))), (X3 + k*int(D*5.8), Y3 + int(D*(-1.4))))
    polygon(screen, GREEN, [(X3 + k*int(D*5.2), Y3 + int(D*(-0.8))), (X3 + k*int(D*4.9), Y3 + int(D*(-1.1))), (X3 + k*int(D*4.9),Y3 + int(D*(-1.4))), (X3 + k*int(D*5.2), Y3 + int(D*(-0.8)))])
    
alien(250, 300, 0.7, 1)
alien(150, 350, 0.3, 1)
alien(50, 350, 0.3, -1)
alien(110, 480, 0.5, -1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()