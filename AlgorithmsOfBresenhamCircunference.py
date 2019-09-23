import pygame
import random

ANCHO = 640
ALTO = 400
centrox =320 
centroy =200

def BresenhamCircle(xc,yc,r):
    # Window dimensions
    width = 640
    height = 400

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    while running:
        x = 0 + xc
        y = r + yc
        p = 2*(x + 1)*(x + 1) + y*y + (y-1)*(y-1) - 2*r*r
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        screen.set_at((centrox+  x, centroy - y), (red, green, blue))
        screen.set_at((centrox + xc,centroy - yc), (red, green, blue))

        while x<=y:
            x = x + 1 #siempre incrementamos en unidades enteras a x
            if (p < 0) : #pintamos xi+1,yi
                p = p + 4*x + 10 #segun mi ecuacion
                #p = p + 4*x*x + 12*x + 4*y + 10
            else : #pintamos xi+1,yi-1
                y = y - 1
                p = p + 4*(x - y) + 10
                #p = p + y*y + 4*x - 5*y + 8
            screen.set_at((centrox + (x + xc),centroy- y - yc), (red, green, blue))
            screen.set_at((centrox+(-x + xc),centroy-(y + yc)), (red, green, blue))
            screen.set_at((centrox+(x + xc),centroy-(-y + yc)), (red, green, blue))
            screen.set_at((centrox+(-x + xc),centroy-(-y + yc)), (red, green, blue))
            screen.set_at((centrox+(y + xc),centroy-(x + yc)), (red, green, blue))
            screen.set_at((centrox+(-y + xc),centroy-(x + yc)), (red, green, blue))
            screen.set_at((centrox+(y + xc),centroy-(-x + yc)), (red, green, blue))
            screen.set_at((centrox+(-y + xc),centroy-(-x + yc)), (red, green, blue))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(240)


BresenhamCircle(0,0,100)
