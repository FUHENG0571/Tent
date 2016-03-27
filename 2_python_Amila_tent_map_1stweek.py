import matplotlib
import pylab as pl
import math
import numpy as np
import matplotlib.pyplot as plt


#-------------------------------------------------------------#
# Initial condition
#-------------------------------------------------------------#
x0=np.linspace(0.0,1.0,100)


# List of alpha's
alpha_list=[0.1,0.4,0.8]

#-------------------------------------------------------------#
# Creating zero 3*100 matrices
# I'm going to use columns to represent xN values for different alpha's
# Rows will be different x0 values
#-------------------------------------------------------------#
z0 = np.zeros((100,3))
z1 = np.zeros((100,3))
z2 = np.zeros((100,3))
z3 = np.zeros((100,3))
z4 = np.zeros((100,3))
z5 = np.zeros((100,3))
# z1,z2,... means z-matrix for N=1,2,... iterations

#-------------------------------------------------------------#
#defining the function f(mu)
#-------------------------------------------------------------#
def fmu(x,alpha):
    if x<0.5:
        return 2*alpha*x
    else:
        return 2*alpha*(1-x)


#-------------------------------------------------------------#
# Constructing z-matrices
#-------------------------------------------------------------#

for m in range(3):
    for n in range(100):
        z0[n][m]=x0[n]
        z1[n][m]=fmu(z0[n][m],alpha_list[m])
        z2[n][m]=fmu(z1[n][m],alpha_list[m])
        z3[n][m]=fmu(z2[n][m],alpha_list[m])
        z4[n][m]=fmu(z3[n][m],alpha_list[m])
        z5[n][m]=fmu(z4[n][m],alpha_list[m])

#-------------------------------------------------------------#
# Plotting
#-------------------------------------------------------------#

# Each column is for different alpha

plt.subplot(3, 1, 1)
plt.plot(x0,z1[:,0],linestyle='-',color='r',label='N=1')
plt.plot(x0,z2[:,0],linestyle='-',color='b',label='N=2')
plt.plot(x0,z3[:,0],linestyle='-',color='g',label='N=3')
plt.plot(x0,z4[:,0],linestyle='-',color='m',label='N=4')
plt.plot(x0,z5[:,0],linestyle='-',color='c',label='N=5')
plt.xlabel('$X_0$')
plt.ylabel('$X_N$')
plt.title(r'$\alpha$ = 0.1')
plt.legend(loc='upper right')

plt.subplot(3, 1, 2)
plt.plot(x0,z1[:,1],linestyle='-',color='r',label='N=1')
plt.plot(x0,z2[:,1],linestyle='-',color='b',label='N=2')
plt.plot(x0,z3[:,1],linestyle='-',color='g',label='N=3')
plt.plot(x0,z4[:,1],linestyle='-',color='m',label='N=4')
plt.plot(x0,z5[:,1],linestyle='-',color='c',label='N=5')
plt.xlabel('$X_0$')
plt.ylabel('$X_N$')
plt.title(r'$\alpha$ = 0.4')
plt.legend(loc='upper right')

plt.subplot(3, 1, 3)
plt.plot(x0,z1[:,2],linestyle='-',color='r',label='N=1')
plt.plot(x0,z2[:,2],linestyle='-',color='b',label='N=2')
plt.plot(x0,z3[:,2],linestyle='-',color='g',label='N=3')
plt.plot(x0,z4[:,2],linestyle='-',color='m',label='N=4')
plt.plot(x0,z5[:,2],linestyle='-',color='c',label='N=5')
plt.xlabel('$X_0$')
plt.ylabel('$X_N$')
plt.title(r'$\alpha$ = 0.8')
plt.legend(loc='upper right')

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.show()