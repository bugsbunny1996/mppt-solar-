import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt 
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
import collections
from scipy.signal import argrelextrema
import math 
from matplotlib.figure import Figure
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import sys
import subprocess
import datetime

def convert(wss):
	x = []
	for y in wss:
		z = []
		z.append(y)
		x.append(z)
	return x

#Variables 
P =list() #power
L =list() #Load
V =list() #Voltage
I =list() #Current 

#Train dats 
with open('solar.txt') as w:
	k = np.asarray(w.readlines(),np.float)
ws = [x * 360 for x in k]

with open('temp.txt') as t:
	te = np.asarray(t.readlines(),np.float)

#machine learning part 
#DATA WILL BE TRAINED CONTINUOUSLY TAKING THE DATA SET OF EVERY 2 HOUR DATA
#data containing the present trainset from 1st 125 minutes = 2 hour dataset

traindata = convert(ws)
loaddata =convert(ld)

import time 
jtag = time.time()

regr_1 = DecisionTreeRegressor(max_depth=1000)
regr_1.fit(traindata, loaddata)

timelapse = time.time() - jtag 

predict= []
freeinput = []
simulate = []

#plotting real time with 4 different wind sets 

import random
for i in range (1, 100):
	freeinput.append(i)
	temp = random.randint(400,440)
	predict.append(np.float(regr_1.predict([temp])))
	simulate.append(pando(0,temp))

plt.title(" Power Vs. time (s)")
plt.ylabel("Power ( Watts ) ")
plt.xlabel("Time in ( seconds )")
plt.plot(freeinput,predict,"r")
plt.plot(freeinput,simulate,"b")
plt.show()
