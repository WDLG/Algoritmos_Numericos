import math
import numpy as np
import matplotlib.pyplot as pyplot
import thread
import time
#Autor: Andres Velasco
#Fecha: 18/08/2017

a=0
b=0
c=0


def ElipsePolar(o):
    return a*b/math.sqrt(((b*math.cos(o))**2)+((a*math.cos(o))**2))

def graficar():
    print "-------------------------------HILO 3-------------------------------------------"
    print "*En este hilo se realiza el grafico"
    w=2*a/100000000
    h=b/100000000
    sol=((((147098290000-152098232000)/100000000)),0)
    x=np.arange(-w,w)

    pyplot.plot(x, [ElipseEscPos(i,w,h) for i in x])
    pyplot.plot(x, [ElipseEscNgt(i,w,h) for i in x])
    pyplot.plot([(147098290000-152098232000)/100000000], [0], marker='o', markersize=3, color="red")
    pyplot.xlim(-2*w,2*w)
    pyplot.ylim(-2*h,2*h)
    pyplot.show()

def ElipseEscPos(x,w,h):
	return math.sqrt((h**2)*((w**2)-(x**2))/(w**2) )

def ElipseEscNgt(x,w,h):
	return math.sqrt((h**2)*((w**2)-(x**2))/(w**2) )*(-1)

def Calcular_a_b_c(Afelio,Perifelio):
	global a
	global b
	global c
	a=(Afelio+Perifelio)/2
	c=a-Perifelio
	b=math.sqrt((a**2) - (c**2))

def Elipse(x):
	return math.sqrt((b**2)*((a**2)-(x**2))/(a**2) )

def Logitud(x):
	if x!=a:
		return math.sqrt(1+(( b**2)*(x**2))/((a**2)*((a**2)-(x**2))+0.0))
	else:
		return 0

def diferencial(n,p,q):
	return (q-p)/(n+0.0)

def ti(n,i,p,q):
    return Logitud(p+i*diferencial(n,p,q))

def integral(n,p,q,dt):
    print "-------------------------------HILO 1-------------------------------------------"
    Longitud=0
    Inte=0
    for i in range(1,n+1):
        Inte=Inte+ti(n,i,p,q)

    Longitud=4*(Inte*diferencial(n,p,q))
    Rapidez=Longitud/(dt+0.0)
    print "El perimetro es: "+str(Longitud)+ " metros"
    print "La rapidez es: "+str(Rapidez)+ " m/s equivalente a:  "+str(Rapidez/1000)+ " km/s"


def momentosAngular():
    print "-------------------------------HILO 2-------------------------------------------"
    m=5.9722*(10**24)
    r=6378.1*1000
    angulos=np.arange(0,math.pi,dtype=float)
    for angulo in angulos:
        R=ElipsePolar(angulo)
        print "Momento angular para r=: "+str(R)+" es: "+str(m*(r**2)*R)
        guardarArchivo(str(m*(r**2)*ElipsePolar(angulo)))

def guardarArchivo(info):
    archivo = open("momentos.txt", "a")
    archivo.write(str(info)+"\n")

def main():
    dt=31556925.9072
    Afelio=152098232000
    Perifelio=147098290000
    Calcular_a_b_c(Afelio,Perifelio)
    p=0
    q=a
    try:
        r1=thread.start_new_thread( integral,(1000,p,q,dt))
        time.sleep(1)
        r2=thread.start_new_thread( momentosAngular,())

        graficar()
        time.sleep(2)
    except:
        print "Error en un hilo"

main()
