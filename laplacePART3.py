#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 11:36:59 2025

@author: dustindocusen
"""

import numpy as np
from matplotlib import pyplot as pp
from matplotlib.animation import FuncAnimation as FA


dx = dy = 0.1
a,b = 10,10
maxV = 1
x = np.arange(0, dx + a, dx, dtype=float)
y = np.arange(0, dy + b, dy, dtype=float)
mid = len(x)/2
h = 25

X,Y = np.meshgrid(x,y)

V = np.zeros_like(X)

deltaV = np.inf

fig = pp.figure()
ax = fig.add_subplot(projection='3d')

def init():
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    return []

def update(m):
    global V, deltaV
    
    if deltaV < 0.001:
        return
    
    newV = np.zeros_like(V)
    newV[:,0] = 0
    newV[:,-1] = 0
    newV[-1,:] = 0
    newV[0,:] = 0

    for i in range(1, V.shape[0]-1):
        for j in range(1, V.shape[1]-1):
            newV[i,j] = (1/4)*(
                V[i+1,j] + V[i-1,j] +
                V[i,j+1] + V[i,j-1]
                )
    newV[h:-h,int(mid*(2/3))] = 1
    newV[h:-h,int(mid*(4/3))] = -1
    
    deltaV = np.max(np.abs(newV - V))
    
    V = newV
    ax.cla()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('V')
    ax.plot_surface(X,Y,V,cmap='viridis')

    return 


myanim = FA(fig,update,init_func=init,interval=1)

pp.show()