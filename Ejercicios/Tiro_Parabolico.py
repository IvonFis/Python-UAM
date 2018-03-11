'''
Un codigo resuelve la ecuacion de tirio parabolico
'''

import sys

x0 = float(sys.argv[1])
y0 = float(sys.argv[2])
v0x = float(sys.argv[3])
v0y = float(sys.argv[4])
t0 = int(sys.argv[5])
tf = int(sys.argv[6])
g = 9.81

def x(t):
    return x0 + v0x*t

def y(t):
    return y0 + v0y*t

for i in range(t0,tf,1):
    print(i,x(i),y(i))

