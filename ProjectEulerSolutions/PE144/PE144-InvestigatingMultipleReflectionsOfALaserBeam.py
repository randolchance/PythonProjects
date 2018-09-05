# PROJECT EULER PROBLEM 144 -

import sys
import os
sys.path.insert(0,os.path.expanduser("~/PythonProjects/venvGMPY2/lib/python3.5/site-packages"))
from gmpy2 import *
from time import sleep

#print(get_context())
get_context().precision=400

ROUND_PREC = 12

pi = const_pi()

def slope(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1    
    return(div(dy,dx) if abs(dx) != 0 else inf(dy))

def perp_slope(m): return(div(-1,m))

def mElipse(x,y):
    return(-4*div(x,y) if abs(y) != 0 else inf(-x))

def slopeReflection(m,m_i):
    theta = pi
    theta += pi if is_infinite(m) else 2*atan(m)
    theta -= div(pi,2) if is_infinite(m_i) else atan(m_i)
    return(tan(theta))

def solveX(m,X,Y):
    if m == inf(): return(X)
    m2 = m**2
    d = m2 + 4
    p = m2*X - m*Y
    pm = 2*sqrt(100 + (25 - X**2)*m2 + 2*m*X*Y - Y**2)
    x1 = div(p+pm,d)
    x2 = div(p-pm,d)
    x = x1 if round(X,ROUND_PREC) == round(x2,ROUND_PREC) else x2
    return(x)

def solveY(m,x,X,Y):
    _y = sqrt(100-4*x**2)
    M = round(slope(X,Y,x,_y),ROUND_PREC)
    m = round(m,ROUND_PREC)
    return(_y if M == m else -_y)

EXIT_x = 0.01

def checkVictory(x,y): return(x >= -EXIT_x and x <= EXIT_x and y > 0)

def f(x): return(round(x,ROUND_PREC//4))

y0 = 10.1
x0 = 0.0
y = -9.6
x = 1.4
m_i = slope(x0,y0,x,y)

victory = False
bounces = 0
while not victory:
    bounces += 1
    m = mElipse(x,y)
    m_r = slopeReflection(m,m_i)
    if round(m_r,ROUND_PREC) == 0:
        bounces *= 2
        break
    next_x = solveX(m_r,x,y)
    next_y = solveY(m_r,next_x,x,y)
    x = next_x
    y = next_y
    victory = checkVictory(x,y)
    m_i = m_r

print(bounces)

