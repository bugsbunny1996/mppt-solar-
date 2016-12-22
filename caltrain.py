from __future__ import division
import numpy as np
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
	
with open('temperature.txt') as t:
	te = np.asarray(t.readlines(),np.float)
with open('solar.txt') as s:
	se = np.asarray(s.readlines(),np.float)

f = open('traindata.txt','w')

for i in range(0,11000):
	da = np.float(se[i])
	ta = np.float(te[i])
	temp = np.float(pando(0.0	,da,ta))
	f.write(str(temp))
	f.write('\n')

f.close()
	