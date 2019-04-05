import matplotlib.pyplot as plt
import numpy as np
import array as arr
import math


def myDelta(n):
    return(n==0)

def myU(n):
    return(n>=0)

def mySin(n,f):
   return math.sin(2*(math.pi)*n*f)

def mySistem(n , x,f,a,b):
    solution=arr.array('d')
    for i in n:
        ypree=0
        ypre=0
        preb=i-1
        prebb=i-2
        if preb>=0:
            ypre=solution[preb]
        if prebb>=0:
            ypree = solution[prebb]
        d=0.5*x(i-2,f)
        solution.append(d+(a*ypre)+(b*ypree))



    return solution



t1 = np.arange(100)
frec=np.arange(0.001,0.5,0.0001)
rtafrec=arr.array('d')

for i in frec:
    semiSol=mySistem(t1 , mySin,i,1,-0.5)
    semiSol=semiSol[30:99]
    rtafrec.append(20*math.log10(max(semiSol)))


l = plt.plot(frec,rtafrec, 'ro')
plt.xlabel('Frecuencia[Hz]')
plt.ylabel('atenuacion [dB]')
plt.title('Respuesta en frecuencia')
plt.semilogx()
plt.setp(l, markersize=10)
plt.setp(l, markerfacecolor='C0')

plt.show()