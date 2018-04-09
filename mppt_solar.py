from __future__ import division
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
def convert(wss):
	x = []
	for y in wss:
		z = []
		z.append(y)
		x.append(z)
	return x

def Pow(v,g,t):
	k = float(1)
	k = np.float(t/300)
	Iph = g * 241.935 * 1e-4*(1.6/4.88)
	i = (-1e-9*(2.73**(v/(0.0258*k)) - 1) + Iph)
	P = v * i
	if g is 0:
		return 0
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

with open('traindata.txt') as load:
	ld = np.asarray(load.readlines(),np.float)

with open('solar.txt') as se:
	solar = np.asarray(se.readlines(),np.float)

with open('temperature.txt') as tem:
	te = np.asarray(tem.readlines(),np.float)
	
z = list()
for i in range(0,11000):
	z.append(np.float(solar[i]) * np.float(te[i])) 

ld = convert(ld)
z = convert(z)
regr_1 = DecisionTreeRegressor(max_depth=1000)
regr_1.fit(z,ld)
freeinput = list()
simulate = list()
predict = list()

#Power vs Iteration graphs
'''
import random
for i in range (1, 1000):
	freeinput.append(i)
	temperature = random.randint(290,310)
	irradiance = random.randint(500,800)
	predict.append(regr_1.predict([irradiance * temperature ] ))
	simulate.append(pando(0,irradiance,temperature))
	
plt.plot(freeinput,predict,"m")
plt.plot(freeinput,simulate,"b")
plt.show()
'''

#Error calculation in constant temperature 298.15K 

for i in range(1,800):
	freeinput.append(i)
	var = np.array(298.15 * i).reshape(1,-1)
	p=regr_1.predict(var)
	var2 = pando(0,i,300)
	error = var2 - np.float(p)
	predict.append(error/var2)
plt.plot(freeinput,predict)
plt.show()

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

#Mean Error calculation as time goes at Room temperature
predict = [0]
freeinput = [0]
for count in range (1,3000):
	
	with open('solar.txt') as w:
		se = np.asarray(w.readlines()[:count],np.float)
	with open('traindata.txt') as load:
		ld = np.asarray(load.readlines()[:count],np.float)
	with open('temperature.txt') as temp:
		te = np.asarray(temp.readlines()[:count],np.float)
	z = list()
	for i in range(0,count):
		z.append(np.float(se[i]) * np.float(te[i])) 
	ld = convert(ld)
	z = convert(z)
	regr_1 = DecisionTreeRegressor(max_depth=1000)
	regr_1.fit(z,ld)
	var = np.array(300 * 500)
	var = var.reshape(1,-1)
	p= regr_1.predict(var)
	var2 = np.float(pando(0,500,300))
	error = var2 - np.float(p)
	if error < 0:
		error = -error
	predict.append(error/var2)
	freeinput.append(count)

T = freeinput
power = predict

from scipy.interpolate import spline
xnew = np.linspace(1,400,10000)
power_smooth = spline(T,power,xnew)

plt.title(" Learning Curve")
plt.ylabel("Error")
plt.xlabel("Iteration")
plt.plot(xnew,power_smooth,"r")
plt.show()
'''