#Autor: Andres Velasco
#Autor: Andres Velasco
import numpy as np


#Genera las matrices D y R
def generarDR(m):
    D=np.zeros((m.shape[0],m.shape[0]),dtype=float)    
    R=np.zeros((m.shape[0],m.shape[0]),dtype=float)    
    for i in range(0,m.shape[0]):
        for j in range (0,m.shape[0]):
            if i==j:    
                D[i][j]=m[i][j]
            else:    
                R[i][j]=m[i][j]
    #Retorna una arreglo de matrices con D y R
    return np.array([D,R],dtype=float)   

#Obtiene la matriz inversa de la matriz D
def GetDi(m):
     D=np.zeros((m.shape[0],m.shape[0]),dtype=float)    
     for i in range(0,m.shape[0]):
        for j in range (0,m.shape[0]):
            if i==j:    
                D[i][j]=1/m[i][j]
     return D
#Genera un vector x con 1s
def generarX(n):
    x=np.zeros((n),dtype=float)
    for i in range(0,n):
        x[i]=1
    return x  

#Funcion main
def main():
    #Inicializo la matriz A y la matriz b de forma aleatoria
    #A=np.array(np.random.randint(1,20,size=(4, 4)),dtype=float)
    #b=np.array(np.random.randint(1,20,size=4),dtype=float)
    
    #Inicializo m y b
    A=np.array([[5,-1,2],[3,8,-2],[1,1,4]],dtype=float)
    b=np.array([12,-25,6],dtype=float)
    print "Matriz A (parte dependiente del sistema)"
    print A
    print "Matriz b (parte independiente del sistema)"
    print b 
    
    #Generacion de datos
    M=generarDR(A)
    D=M[0]
    R=M[1]
    Di=GetDi(M[0])
    xo=np.zeros((A.shape[0]),dtype=float)
    x=generarX(A.shape[0])

    while np.array_equal(x,xo)!=True:
        xo=x
        x=np.dot(Di,(b-np.dot(R,x)))

    print "Soluciones al sistema de ecuaciones:"    
    print x
main()