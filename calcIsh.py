import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure
import sys
sys.maxint
ni2 = 10**20
e = 1.6 * 10**(-19) 
T = 0
De = 34.93*(T/298.15)*10**(-4)
Dh = 11.64*(T/298.15)*10**(-4)
Le = 1.9*(T/298.15)**(1/2)
Lh = 1.08*(T/298.15)**(1/2)
Na = 10**16
Nd = 10**15

Ish = list()
x = list()
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
	