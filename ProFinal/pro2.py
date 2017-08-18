import math
import thread
import time
#Autor: Andres Velasco
#Fecha: 18/08/2017

lista=[0,0,0,0]
a=0.2
b=0.4
c=0.6
d=0.8
e=1
densidad=890
n=100000



def Ecuacion(y):
    return 2*y*(math.sqrt(1-y**2))

def sumarLista():
    suma=0
    for x in lista:
        suma=suma+float(x)
    return suma

def diferencial(n,p,q):
	return (q-p)/(n+0.0)

def ti(n,i,p,q):
    return Ecuacion(p+i*diferencial(n,p,q))

def IntegralParcial(k,l,num):
    global lista
    lista[num]=integral(n,k,l,densidad)

def integral(n,p,q,densidad):
    Presion=0
    inte=0
    gravedad=9.8
    for i in range (1,n+1):
        inte=inte+ti(n,i,p,q)
    inte=inte*diferencial(n,p,q)
    Presion=densidad*gravedad*inte
    print "La Fuerza Parcial es: "+str(Presion)+" N"
    return Presion


print "-------------------------------------------------------"
print"RESULTADOS PARCIALES:"
print "-------------------------------------------------------"

try:
    r1=thread.start_new_thread( IntegralParcial,(a,b,0))
    r2=thread.start_new_thread( IntegralParcial,(b,c,1))
    r3=thread.start_new_thread( IntegralParcial,(c,d,2))
    r4=thread.start_new_thread( IntegralParcial,(d,e,3))

    time.sleep(2)
    print "-------------------------------------------------------"
    print"RESULTADO DEFINITIVO:"
    print "-------------------------------------------------------"
    print "El valor de la fuerza es: "+str(sumarLista())+" N"
except:
    print "Error: unable to start thread"
