from math import *
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def EqDif (Y,T):
	x = Y[0]
	vx = Y[1]

	y = Y[2]
	vy = Y[3]

	dxdt = vx
	dvxdt = 0

	dydt = vy
	dvydt = -g



	return [dxdt,dvxdt,dydt,dvydt]


def EqDif2 (Z,T):
	x = Z[0]
	vx = Z[1]

	y = Z[2]
	vy = Z[3]

	Fa = Z[4]

	Fm = Z[5]

	w = (2*pi)*3
	r = 0.1192
	p = 1.1839
	Ca = 0.45
	A = pi*(r**2)

	v = (((vx**2) + (vy**2))**(1/2))

	Fa = (Ca * p * A * (v**2))/2

	Fm = (4/3)*(4*(pi**2)*(r**3)*w*p*v)

	dxdt = vx
	dvxdt = ((-Fa *(vx/v)) + (-Fm*(vy/v)))/m

	dydt = vy
	dvydt = ((-g*m) + ((-Fa *(vy/v))) + (Fm*(vx/v)))/m


	return [dxdt,dvxdt,dydt,dvydt,Fa,Fm]

g = 9.8
m = 0.623
ang = 55
teta = ang*pi/180
vo = 7
vox = vo * cos(teta)
voy = vo * sin(teta)
Y0 = [0,vox,1.8,voy]
Z0 = [0,vox,1.8,voy,0,0]
T = np.arange(0,1.2 ,0.01)


sol = odeint(EqDif,Y0,T) 
sol2 = odeint(EqDif2,Z0,T)

plt.plot(T,sol[:,2],'r--', label = 'Desprezando as forças')

plt.plot(T,sol2[:,2], label = 'Com as forças de arrasto e de Magnus (backspin)')

plt.ylabel("Deslocamento em y")
plt.xlabel("Tempo")
plt.title("Movimento vertical x Tempo")
plt.legend()
plt.grid()
plt.show()

plt.plot(T,sol2[:,5])
plt.title("Força Magnus x tempo")
plt.grid()
plt.xlabel("Tempo (s)")
plt.ylabel("Força (N)")
plt.show() 