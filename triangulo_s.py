# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rng

n=100000

coordx=[]
coordy=[]

seedx=0.5
seedy=0.66

coordx.append(seedx)
coordy.append(seedy)

mitadx=0
mitady=0

v1x=0
v1y=0
v2x=0.5
v2y=np.sqrt(3)/2
v3x=1
v3y=0

r=[]
r=rng(n)

for i in range(n):
    if(r[i]<1/3):
        verticex=v1x
        verticey=v1y
    elif(1/3<r[i]<2/3):
        verticex=v2x
        verticey=v2y
    elif(r[i]>2/3):
        verticex=v3x
        verticey=v3y
    if(i==0):
        mitadx=(verticex+seedx)/2
        mitady=(verticey+seedy)/2
    else:
        mitadx=(verticex+mitadx)/2
        mitady=(verticey+mitady)/2

    coordx.append(mitadx)
    coordy.append(mitady)

plt.plot(coordx,coordy,'b ,')
plt.text(0.1,0.7,r'$n=10000$')