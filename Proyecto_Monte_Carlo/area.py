from random import *
import pygame
import math
pi="3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489"


#Contara el numero de ocurrencias entre el valor de pi Real y el valor calculado
def contDecimales(cad):
    i=0
    while (True):
        if cad[i]!=pi[i]:
            break
        i=i+1
    return i-2

#Calcula la eficiencia
def eficiencia(n,d):
    return n/d


def coord(x,y):
    #Convierte coordenadas rectangulares a coordenadas de pixel
    return 300+300*x,300+300*y

    #Metodo que evalua un punto en la ecuaccion del circulo
def circleEc(x,y):
    return math.sqrt(x**2 + y**2)

    #Grafica la generacion de puntos a 20 cuadros por segundo
def dibujar(lista,n):
    pygame.init()
    pantalla = pygame.display.set_mode((800,800))
    listarec=[]

    BLUE  = (  255,   255, 255)
    for punto in lista:
        w=2
        h=2
        x=punto[0]
        y=punto[1]
        (x,y)=coord(x,y)
        listarec.append(pygame.Rect(x,y,w,h))

    salir=False
    reloj1=pygame.time.Clock()
    while salir!=True:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 salir=True
             else:
                reloj1.tick(60)
                pantalla.fill((192,192,192))
                pygame.draw.circle(pantalla, BLUE, (300,300),300, 0)
             for recs in listarec:
                 if circleEc(recs.x-300,recs.y-300) <= 300:
                    pygame.draw.rect(pantalla,(255,0,0),recs)
                 else:
                    pygame.draw.rect(pantalla,(0,255,0),recs)
                 pygame.display.update()


    pygame.quit()



n=1000000

numero=0.0000000000000000000000000000
contd=0.000000000000000000000000
lista=list()
for i in range(0,n):
    x=uniform(-1,1)                                                          #Genera un valor aleatorio entre -1 y 1 para x
    y=uniform(-1,1)                                                          #Genera un valor aleatorio entre -1 y 1 para y
    point=(x,y)                                                              #Crea el punto con x y y
    prueba=pow(x,2)+pow(y,2)                                                 #Evalua la ecuacion del circulo
    if (prueba <= 1):                                                        #Pregunta si el punto generado se encuentra dentro del circulo
	    contd=contd+1                                                        #Cuenta el numero de puntos dentro del circulo
    lista.append(point)
aux=float(contd/n)                                                           #Calcula la relacion entre los puntos dentro del circulo y el total de puntos
numero=float(aux*4)                                                          #Calcula el area del circulo
print("El area del circulo con "+str(n)+" puntos es: "+str(numero))          #Imprime el area del circulo
print "La eficiencia de es "+str(eficiencia(n,contDecimales(str(numero))))+" para cada decimal"
dibujar(lista,n)
