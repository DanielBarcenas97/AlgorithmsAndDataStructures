vimport pygame
import sys
import copy
import libreria1

ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
BLANCO = (255,255,255)
NEGRO = (0,0,0)

def BresenhamCircle(xc,yc,r):#xcentro, ycentro, radio
    #iniciamos en 0,r
    x = 0 + xc
    y = r + yc
    #p = 1 - r
    p = 2*(x + 1)*(x + 1) + y*y + (y-1)*(y-1) - 2*r*r
    p_new = [[xc,yc],[x,y]]
    libreria1.DrawPixel(libreria1.Transform(p_new[0]), VERDE)
    libreria1.DrawPixel(libreria1.Transform(p_new[1]), VERDE)
    #se cicla hasta trazar todo un octante
    while (x < y) :
        x = x + 1 #siempre incrementamos en unidades enteras a x
        if (p < 0) : #pintamos xi+1,yi
            p = p + 4*x + 10 #segun mi ecuacion
            #p = p + 4*x*x + 12*x + 4*y + 10
        else : #pintamos xi+1,yi-1
            y = y - 1
            p = p + 4*(x - y) + 10
            #p = p + y*y + 4*x - 5*y + 8

        libreria1.DrawPixel(libreria1.Transform([x + xc,y + yc]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([-x + xc,y + yc]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([x + xc,-y + yc]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([-x + xc,-y + yc]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([y + xc,x + yc]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([-y + xc,x + yc]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([y + xc,-x + yc]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([-y + xc,-x + yc]), VERDE)


libreria1.makePlane()

BresenhamCircle(10,10,100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)