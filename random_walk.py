import pygame, math
from random import randint, seed

#seed(1031)

running = 1
width = 1600
height = 1000
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()
depth = 901

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0, 255)

xg = width / 2
yg = height / 2

ticker = 10
draw = 1

def empty():
    return 0

def walk(x, y, size, depth):
    if depth:
        UD = randint(0, 1)
        if UD == 0: #down
            y2 = y + (size * -1)
        else:
            y2 = y + size
        x2 = x + size
        pygame.draw.line(screen, WHITE, (x, y), (x2, y2), 2)
        walk(x2, y2, size, depth - 1)

def wander(x, y, size, depth):
    global xg, yg
    if depth:
        UD = randint(0, 3)
        if UD == 0: #down
            y2 = y + (size * -1)
            x2 = x
        elif UD == 1: #left
            y2 = y
            x2 = x + (size * -1)
        elif UD == 2: #up
            y2 = y + size
            x2 = x
        else: #right
            y2 = y
            x2 = x + size
        pygame.draw.line(screen, BLUE, (x, y), (x2, y2), 2)
        xg = x2
        yg = y2
        wander(x2, y2, size, depth - 1)


screen = pygame.display.set_mode((width, height))
screen.fill((BLACK))

#GAMELOOP
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            print "Doing walk!"
            walk(300,300,2,depth)
        if event.key == pygame.K_o:
            print "Doing wander!"
            wander(xg,yg,15,depth)
        if event.key == pygame.K_r:
            print "RESET!"
            xg, yg = width / 2, height / 2
        if event.key == pygame.K_c:
            screen.fill((BLACK))

    move_ticker = 0
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if move_ticker == 0:
            move_ticker = ticker
            move_ticker = ticker
            walk(xg,yg,2,depth)
    if keys[pygame.K_UP]:
        if move_ticker == 0:
            move_ticker = ticker
            move_ticker = ticker
            wander(xg,yg,0.5,depth)

    pygame.display.update()
    fpsClock.tick(FPS)