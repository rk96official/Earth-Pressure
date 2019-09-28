import scipy.integrate as integrate
import numpy as np
import matplotlib.pylab as plt
import math
x=0.0
def f(x):
    res=integrate.quad(lambda x: np.cos (x),math.pi/2,2*math.pi)
    num=str(round(res[0],2))
    return num
def g(t,u):
    return np.cos (t-u)
ans,ress=integrate.dblquad(g,0,2*math.pi, lambda u:0 ,lambda u:2*math.pi)
answer = str(round(ans, 2))
def h(t,u,v):
    return np.cos (t-u-v)
answ,resss=integrate.tplquad(h,0,math.pi, lambda u:0 ,lambda u:math.pi, lambda u,v:0,lambda u,v:math.pi)
answ = str(round(answ, 2))
print(f(x))
print(answer)
print (answ)

x=np.linspace(-math.pi,math.pi,1000)
y=np.sinh(x)
z=np.cosh(x)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,y)
plt.plot(x,z)
plt.show()
