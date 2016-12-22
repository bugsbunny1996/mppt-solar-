import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure	
import sys
sys.maxint
ni2 = 10**20
e = 1.6 * 10**(-19) 
Na = 10**16
Nd = 10**15
Ish = list()
Q		 = list()
'''
for T in range (0,1000):
	De = 34.93*(T/298.15)*10**(-4)
	Dh = 11.64*(T/298.15)*10**(-4)
	Le = 1.9*(T/298.15)**(1/2)
	Lh = 1.08*(T/298.15)**(1/2)

	temp = ni2*e * ( De/(Le*Na) + Dh/(Lh*Nd))
	Ish.append(temp)
	x.append(T)
plt.plot(x,Ish,"b")
plt.show()
'''
G = 600
P = list()
Iph = G * 241.935 * 10**(-4)*(1.6/4.88)
k = 1.3807 * 10**(-23)
Rl = 10
Rs = 10
for x in range (0, 20):
	T = 300
	Ish = 10**(-9)
	temp = x*(-1*10**(-9)*(2.73**(x/0.0258*0.8) - 1) + 3.1)
	P.append(temp)
	Q.append(x)
	
	
plt.plot(Q,P,"b")
plt.show()

