import thread
import time
import integral as it
import math

#Define a function for the thread
n=1000
a=0
b=1
c=2
d=3
e=4
sumtot=0
sum1=0
lista=[0,0,0,0]

def IntegralParcial(x,y,num):
    print ""
    print "valor de la integral parcial: "+str(it.Integral(n,x,y))
    lista[num]=it.Integral(n,x,y)


def sumarLIsta():
    suma=0
    for x in lista:
        suma=suma+float(x)
    return suma

try:
    r1=thread.start_new_thread( IntegralParcial,(a,b,0))

    r2=thread.start_new_thread( IntegralParcial,(b,c,1))

    r3=thread.start_new_thread( IntegralParcial,(c,d,2))

    r4=thread.start_new_thread( IntegralParcial,(d,e,3))

    time.sleep(1)

    print sumarLIsta()
except:
    print "Error: unable to start thread"
