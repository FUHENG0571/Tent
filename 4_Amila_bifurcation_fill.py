import matplotlib
import pylab as pl
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

#-------------------------------------------------------------#
# Initial condition
#-------------------------------------------------------------#

x0=0.2


# List of alpha's
alpha_list=np.linspace(0.1,0.9,81)

# List of N values (Total number of iterations=length of x)
x=range(2000)

# Index corresponding to alpha=0.5
mstart=(len(alpha_list)-1)/2

#-------------------------------------------------------------#
# Creating zero matrices
# I'm going to use columns to represent xN values for different alpha's
# Rows will be different xN values for N=0 to len(x)
#-------------------------------------------------------------#

z=np.zeros((len(x),len(alpha_list)))
z2=np.zeros((len(x),len(alpha_list)))
z3=np.zeros((len(x),len(alpha_list)))


for m in range(len(alpha_list)):
    z[0][m]=x0


#-------------------------------------------------------------#
#defining the function f(mu)
#-------------------------------------------------------------#
def fmu(x,alpha):
    if x<0.5:
        return 2*alpha*x
    else:
        return 2*alpha*(1-x)


#-------------------------------------------------------------#
# Constructing z-matrix, XN's in rows and columns corresponds to alpha values
#-------------------------------------------------------------#

for m in range(len(alpha_list)):
    for n in range(len(x)-1):
        z[n+1][m]= fmu(z[n][m],alpha_list[m])     

# Counting number of times z[n][m] appears in the mth row= z2 matrix
for m in range(len(alpha_list)):
    for n in range(len(x)):
        z1=(((z[n][m]-0.005 < z[:,m]) & (z[:,m] < z[n][m]+0.005)).sum())/500.
        z2[n][m]=z1     
# Normalization:
for m in range(len(alpha_list)):
    rowmax=max(z2[:,m]) # maximum value of a certain row in z2 matrix
    for n in range(len(x)):
        z2elemnt=z2[n][m]
        z3[n][m]=z2elemnt/rowmax # normalized z2 matrix
        
              

#-------------------------------------------------------------#
# Plotting
#-------------------------------------------------------------#

dx=0.005
dy=0.005

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
cmap=plt.get_cmap('Greys')
#cmap = plt.cm.hot

for m in range(mstart,len(alpha_list)):
    for n in range(1000,len(x)):
        ax.add_artist(Rectangle(xy=(alpha_list[m],z[n][m]),color=cmap(z3[n][m]),width=dx,height=dy))
        plt.hold(True) 
plt.axis([0.5,1,0,1])
plt.xlabel('Alpha')
plt.ylabel('$X_N$')
plt.title('Tent Map')
plt.show()