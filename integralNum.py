import math





#Evalua f(x)

def f(x):

    return (math.sin(x))**2



#Evalua el diferencial

def diferencial(n,a,b):

    return (b-a)/(n+0.0)

#Evalua f(ti)

def ti(n,i,a,b):

    return f(a+i*diferencial(n,a,b))



#Calcula el Area bajo la region acotada

def Integral(n,a,b):

    Area=0

    for i in range(1,n+1):

        Area=Area+ti(n,i,a,b)

    Area=Area*diferencial(n,a,b)

    print "El valor de la Integral es: "+str(Area)





a=0

b=2*math.pi

Integral(10000,a,b)
