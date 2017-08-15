import thread
import time
import math
import numpy as np

n=10**7
arr=np.random.randint(1,n,n)
x=0
y=n/4
c=(n/4)+(n/4)
d=(n/4)+(n/4)+(n/4)
e=n
valores=np.array([0,0,0,0],dtype=int)
minimoTotal=0
def minimo(vector,a,b,num):
    minimo=vector[a]
    for x in range (a,b):
        if minimo<vector[x]:
            minimo=minimo
        else:
            minimo=vector[x]

    valores[num]=minimo

def getMinimoTotal(vector,a,b):
    minimo=vector[a]
    for x in range (a,b):
        if minimo<vector[x]:
            minimo=minimo
        else:
            minimo=vector[x]
    return minimo
try:
    thread.start_new_thread( minimo,(arr,x,y,0))
    thread.start_new_thread( minimo,(arr,y+1,c,1))
    thread.start_new_thread( minimo,(arr,c+1,d,2))
    thread.start_new_thread( minimo,(arr,d+1,e,3))
    time.sleep(5)
    print valores
    print getMinimoTotal(valores,0,4)
except:
    print "Error: unable to start thread"
