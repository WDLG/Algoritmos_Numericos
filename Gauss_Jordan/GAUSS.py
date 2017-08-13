import numpy as np
import sys
import random


def guardarArchivo(matriz,n,archivo):
     archivo = open(str(archivo)+".csv", "w")
     for i in range (0,n):
        m=[]
        for j in range (0,n+1):
             if (j!=n):
                 archivo.write(str(matriz[i][j])+",")
             else:
                 archivo.write(str(matriz[i][j]))
        archivo.write("\n")


def generarArchivo(n,nomArchivo):
     matriz=np.random.randint(n,size=(n,n+1))
     m=[]
     archivo = open(str(nomArchivo)+".csv", "w")
     for i in range (0,n):
        m=[]
        for j in range (0,n+1):
             if (j!=n):
                 archivo.write(str(matriz[i][j])+",")
             else:
                 archivo.write(str(matriz[i][j]))
        archivo.write("\n")


#PIVOTEA UNA FILA DE LA MATRIZ Y REDUCE A CEROS
def pivotear(M,i):
    for x in range (0,M.shape[0]):
        if x<i:
            a=M[i][x]
            M[i]=M[i]-a*M[x]
    M[i]=M[i]/M[i][i]
    #print M

#PIVOTEA UNA FILA DE LA MATRIZ Y REDUCE A CEROS DE MANERA INVERSA
def pivotearINV(M,i):
    for x in range (1,M.shape[0]):
        if i!=x:
            a=M[i][x]
            M[i]=M[i]-a*M[x]
    #print M

def leerArchivo(archivo):
    archivo = open(archivo+".csv", "r")
    a=[]
    linea = archivo.readline()
    a.append(linea.split(","))
    while linea != "":
        linea = archivo.readline()
        a.append(linea.split(","))

    a.pop()
    a=np.array(a,dtype=float)

    return a


def main():
    #SISTEMA DE 4 ECUACIONES CON 4 INCOGNITAS
    print sys.argv[1]
    n=sys.argv[1]
    nomarchivo=sys.argv[2]
    archivorespuesta=sys.argv[3]
    generarArchivo(int(n),nomarchivo)
    x = leerArchivo(nomarchivo)
    aux=leerArchivo(nomarchivo)
    #PIVOTEA Y OBTIENE LOS CEROS DE LA PARTE DE ABAJO DE LA MATRIZ
    for j in range (0,x.shape[0]):
        pivotear(x,j)
    #OBTIENE LOS CEROS DE LA PARTE DE ARRIBA DE LA MATRIZ(OBTIENE LA MATRIZ IDENTIDAD)
    for j in range (0,x.shape[0]):
        pivotearINV(x,j)
    guardarArchivo(x,int(n),archivorespuesta)

    print "----------------RESULTADOS DEL SISTEMA DE ECUACIONES-----------------------"
    print "MATRIZ ORIGINAL"
    print"____________________________________________________________________________"
    print aux
    print
    print"____________________________________________________________________________"
    print "MATRIZ IDENTIDAD: "
    print"____________________________________________________________________________"
    print x
    print"____________________________________________________________________________"
    print "DETALLE DE LOS RESULTADOS: "
    print"____________________________________________________________________________"
    j=1
    for i in x:
        print "El valor de la variable "+str(j)+" es: "+str(i[i.shape[0]-1])
        j=j+1

main()
