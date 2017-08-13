from random import *
import math
import pygame

pi="3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489"
#Clase poligo
class Poligono(object):
    def __init__(self,l,r):
        #Cuando se instancie la clase Poligono todos los atributos de un poligono se calcularan
        self.__AnguloCentral=math.radians((360/(l+0.000)))
        print self.__AnguloCentral
        print (self.__AnguloCentral * l / 2)
        self.__Numlados=l
        self.__r=r
        self.__apotema=self.__r*math.cos(self.getAnguloCentral()/2)
        self.__arista=2*r*self.__r*math.sin(self.getAnguloCentral()/2)
        self.__perimetro=self.getNumLados()*self.getArista()

    #Metodos getter puesto que los atributos del poligono estan en private
    #Retorna el Radio del poligno
    def getR(self):
        return self.__r
    #Retorna la longitud de la arista
    def getArista(self):
        return self.__arista
    #Retorna el numero de lados
    def getNumLados(self):
        return self.__Numlados
    #Retorna el angulo central
    def getAnguloCentral(self):
        return self.__AnguloCentral
    #Retorna el perimetro
    def getPerimetro(self):
        return self.__perimetro
    #Retorna el apotema del poligono
    def getApt(self):
        return self.__apotema
    #Calula y Retorna el area del poligono
    def getArea(self):
        return self.getPerimetro()*self.getApt()/2



#Genera puntos aleatorios dentro de la region dada
def generarPunto(n,Poligono):
    x=uniform(-Poligono.getArista()/2,Poligono.getArista()/2)
    z=uniform(Poligono.getApt(),n)
    return (x,z)

#Metodo que evalua un punto en la ecuaccion del circulo
def circuloEc(x,y):
    return math.sqrt(x**2 + y**2)
#Area del rectangulo (Region de generacion de puntos)
def areaRectangulo(Poligono):
    return (Poligono.getR()-Poligono.getApt())*Poligono.getArista()


#Metodo principal que calulara el valor de pi
def calcularSuperficie(l,n):
    r=1
    contPuntos=0
    listaPuntos=list()

    poligono=Poligono(l,r)
    for x in range (0,n+1):
        punto=generarPunto(r,poligono)
        if circuloEc(punto[0],punto[1]) < r:
            contPuntos=contPuntos+1

        listaPuntos.append(punto)
    probabilidad=contPuntos/(n+0.000000)
    areaParcial=areaRectangulo(poligono)*probabilidad*l
    print "Puntos dentro de la region circular marcada: "+str(contPuntos)
    print "Area Parcial: "+str(areaParcial)
    print "Area del Poligono: "+str(poligono.getArea())
    print "Area total: "+str(areaParcial+poligono.getArea())
    print "La eficiencia es: "+str(eficiencia(n,contDecimales(str(areaParcial+poligono.getArea()))))+" itercaciones para cada decimal"
    #dibujar(listaPuntos,n)

#Contara el numero de ocurrencias entre el valor de pi Real y el valor calculado
def contDecimales(cadena):
    i=0
    while (True):
        if cadena[i]!=pi[i]:
            break
        i=i+1
    return i-2

#Calcula la eficiencia
def eficiencia(n,d):
    return n/d


def coord(x,y):
    #Convierte coordenadas rectangulares a coordenadas de pixel
    return 300+300*x,300+300*y

#Grafica la generacion de puntos a 20 cuadros por segundo
def dibujar(lista,n):
    pygame.init()
    pantalla = pygame.display.set_mode((800,800))
    listarec=[]

    GRIS  = (  255,   255, 255)
    for punto in lista:
        w=2
        h=2
        x=punto[0]
        y=punto[1]
        (x,y)=coord(x,y)
        #print "Puntos "+str(x)+","+str(y)
        listarec.append(pygame.Rect(x,y,w,h))

    salir=False
    reloj1=pygame.time.Clock()
    while salir!=True:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 salir=True
             else:
                reloj1.tick(20)
                pantalla.fill((192,192,192))
                pygame.draw.circle(pantalla, GRIS, (300,300),300, 0)
             for recs in listarec:
                 if circuloEc(recs.x-300,recs.y-300) < 300:
                    pygame.draw.rect(pantalla,(255,0,0),recs)
                 else:
                    pygame.draw.rect(pantalla,(0,255,0),recs)
             pygame.display.update()

    pygame.quit()

calcularSuperficie(4000,1000000)
