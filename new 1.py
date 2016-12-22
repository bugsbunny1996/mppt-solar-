from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
import collections
from scipy.signal import argrelextrema
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from decimal import *
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure

#functions 
def Pow(v,g,t):
	k = float(1)
	k = np.float(t/300)
	Iph = g * 241.935 * 1e-4*(1.6/4.88)
	i = (-1e-9*(2.73**(v/(0.0258*k)) - 1) + Iph)
	P = v * i
	return(np.float(P))

def pr(v,g,t):
	P1 = Pow(v,g,t)
	while(1):
		if(Pow(v+0.001,g,t)>P1):
			v=v+0.001
			P1=Pow(v,g,t)
		elif(Pow(v-0.001,g,t)>P1):
			v=v-0.001
			P1=Pow(v,g,t)
		else:	
			break
	return np.float(v)
	
def pando(v,g,t):
	P1 = Pow(v,g,t)
	while(1):
		if(Pow(v+0.001,g,t)>P1):
			v=v+0.001
			P1=Pow(v,g,t)
		elif(Pow(v-0.001,g,t)>P1):
			v=v-0.001
			P1=Pow(v,g,t)
		else:	
			break
	return np.float(P1)		


#Power vs Current vs Voltage graphs 
'''
Iph = 800 * 241.935 * 1e-4*(1.6/4.88)
Q = np.linspace(0, 0.8, 100)
P =  Q * (-1e-9*(2.73**(Q/0.0258*0.9) - 1) + Iph)
R = (-1e-9*(2.73**(Q/0.0258*0.9) - 1) + Iph)
Iph = 700* 241.935 * 1e-4*(1.6/4.88)
Q1 = np.linspace(0, 0.8, 100)
P1 =  Q1 * (-1e-9*(2.73**(Q1/0.0258*1.1) - 1) + Iph)
R1 = (-1e-9*(2.73**(Q1/0.0258*1.1) - 1) + Iph)
Iph = 600 * 241.935 * 1e-4*(1.6/4.88)
Q2 = np.linspace(0, 0.8, 100)
P2 =  Q2 * (-1e-9*(2.73**(Q2/0.0258*1.2) - 1) + Iph)
R2 = (-1e-9*(2.73**(Q2/0.0258*1.2) - 1) + Iph)
Iph = 500 * 241.935 * 1e-4*(1.6/4.88)
Q3 = np.linspace(0, 0.8, 100)
P3 = Q3 * (-1e-9*(2.73**(Q3/0.0258*1.3) - 1) + Iph)
R3 = (-1e-9*(2.73**(Q3/0.0258*1.3) - 1) + Iph)
plt.plot(Q,P)
plt.plot(Q1,P1)
plt.plot(Q2,P2)
plt.plot(Q3,P3)
plt.plot(Q,R)
plt.plot(Q1,R1)
plt.plot(Q2,R2)
plt.plot(Q3,R3)
plt.ylim(0,10)
plt.show()
'''
