import matplotlib
import pylab as pl
import math

#-------------------------------------------------------------#
# Constants
#-------------------------------------------------------------#
x0=0.2
N=19

#-------------------------------------------------------------#
# Initial condition
#-------------------------------------------------------------#
z=[x0,]
y=[x0,]

#-------------------------------------------------------------#
# Defining the function f(mu)
#-------------------------------------------------------------#
def fmu(x,alpha):
    if x<0.5:
        return 2*alpha*x
    else:
        return 2*alpha*(1-x)

fmu(z[0],0.7)

for i in range(N):
    y.append(fmu(y[i],0.4))
    z.append(fmu(z[i],0.7))

    
pl.plot(z,label=r'$\alpha$ = 0.7')
pl.plot(y,label=r'$\alpha$ = 0.4')
pl.legend(loc='lower right')
pl.xlabel('N')
pl.ylabel('$X_N$')
pl.title(r'$X_N$ Vs N')
pl.show()