import math



#Evalua la funcion en un punto de x

def F(x):

    return (math.cos(x))**2



#Evalua el valor de la derivada en un punto de x

def f(x):

    #Valor cercano a cero

    h=0.0000000000000000000000001

    return math.ceil((F(x+h)-F(x+0.00000))/h)



#Calula la recta tangente

def rectangente(x,m):

    y=math.floor(F(x))

    b=-m*x+y

    if m==0:

        print  "Ecuacion es de la rectangente cuando x="+str(x)+" es: y= "+str(b)

    else:

        print  "Ecuacion es de la rectangente cuando x="+str(x)+" es: y="+str(m)+"x "+str(b)



def main():

    x1=0

    x2=math.radians(90)

    m1=f(x1)

    m2=f(x2)

    rectangente(x1,m1)

    rectangente(x2,m2)



main()
