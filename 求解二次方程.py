#coding:utf-8

import math

def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad oprand type')   
    if not isinstance(a,(int,float)):
        raise TypeError('bad oprand type')
    if not isinstance(a,(int,float)):
        raise TypeError('bad oprand type')
    s = b*b - 4*a*c
    if s < 0:
        print ('不存在实数根')
    x1 = (-b + math.sqrt(s))/2*a
    x2 = (-b - math.sqrt(s))/2*a
    return x1,x2
print(quadratic(2,  3,  1))
print(quadratic(1,  3, -4))
print(quadratic(1, -2,  1))

