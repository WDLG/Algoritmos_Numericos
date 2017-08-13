from mpi4py import MPI

import numpy as np

import sys


def generarMatriz(n):

    return np.array(np.random.randint(100, size=(n, n)),dtype=float)

     

def generarMatrizIdentidad(n):

    l=np.zeros((n,n),dtype=float)

    for i in range(0,l.shape[0]): 

        for j in range (0,l.shape[0]):

            if i==j:

                l[i][j]=1



    return l

 

def dividirMatriz(M,n):

    m1=np.zeros((M.shape[0],M.shape[0]),dtype=float)

    m2=np.zeros((M.shape[0],M.shape[0]),dtype=float)

    

    for i in range (0,M.shape[0]):


   if i<M.shape[0]/2:

   m1[i]=M[i]

   else:

   m2[i]=M[i]



    M=np.array([m1,m2],dtype=float)	  

    return M



n=sys.argv[1]

n=int(n)

m=generarMatriz(n)

print m

L=generarMatrizIdentidad(n)

M=dividirMatriz(m,n)

m1=M[0]

m2=M[1]





comm=MPI.COMM_WORLD

rank = MPI.COMM_WORLD.Get_rank()



if rank==0:

   comm.send(m1[0], dest=1, tag=10)

   for i in range (0,m1.shape[0]/2):

       for x in range (0,m1.shape[0]):

           if x<i:

               if i!=0:

          a=m1[x][x]

  L[i][x]=(m1[i][x]/a)

  factor=(m1[i][x]+0.0/a+0.0)

                   m1[i]=m1[i]-(m1[i][x]/a)*m1[x]

  comm.send(m1[i], dest=1, tag=11)



   comm.send(L,dest=1,tag=12)

   



if rank==1:

   m2[0]=comm.recv(source=0,tag=10)

   pivotes=m2[0]

   L=comm.recv(source=0,tag=12)

   for j in range (1,m2.shape[0]/2):

if np.all(m2[j]==0):

  m2[j]=comm.recv(source=0,tag=11)

else:

  break



   for i in range (2,m2.shape[0]):

       for x in range (0,m2.shape[0]):

           if x<i:

     a=m2[x][x]

     factor=(m2[i][x]/a)



     L[i][x]=factor

     



              m2[i]=m2[i]-factor*m2[x]



   print "Matriz Original:"

   print m

   print "Matriz U: "

   print m2

   print "Matriz L:"

   print L

   print "Matriz A=LU"

   print np.dot(L,m2)	  



MPI.Finalize()
