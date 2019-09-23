import pygame
import random

def BresenhamCircleLine(x0,y0,x1,y1):
    width = 640 # Window dimensions
    height = 400
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    while running:
        dx=x1-x0
        dy=y1-y0
        x=x0
        y=y0
        p=2*dy-dx
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        while x<x1:
            if (p >= 0) : #pintamos xi+1,yi
                screen.set_at((x,y), (red, green, blue))
                y=y+1
                p = p+2*dy-2*dx
            else : #pintamos xi+1,yi-1
                screen.set_at((x,y), (red, green, blue))
                p = p + 2*dy
            
            x = x + 1
            #p = p + y*y + 4*x - 5*y + 8
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(240)


BresenhamCircleLine(10,10,200,200)
