import math #Evalua r/(1-r**2)^1/2 
def fr(r):
	 return r/math.sqrt(1-r**2)+0.0 
#Evalua el diferencial 
def diferencial(n,a,b): 
	return (b-a)/(n+0.0) 
#Evalua f(ti) 
def ti(n,i,a,b): 
	if a+i*diferencial(n,a,b) != 1: 
		return fr(a+i*diferencial(n,a,b)) 
	else: 
		return 0 
#Calcula el Area bajo la region acotada 
def Integral(n,a,b): Area=0 
     #Calulamos la integral 
	for i in range(0,n+1): 
		Area=Area+ti(n,i,a,b) 
		Area=Area*diferencial(n,a,b) 
		Areatot=2*math.pi*Area 
		print "El valor de la Integral es: "+str(Areatot) 
#Iniciamos valores a=0 b=1 
Integral(100000,a,b)
