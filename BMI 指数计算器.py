#coding:utf-8
# weight:kg
# hight:m
a = input ('please input your weight:')
b = input ('please input your hight:')
weight = float(a)
hight = float(b)
x = weight / (hight*hight)
if x <= 18.5:
    print ('过轻')
elif x <= 25 and x >18.5:
    print ('正常')
elif x <= 28 and x > 25:
    print ('过重')
elif x <= 32 and x > 28:
    print ('肥胖')
elif x > 32:
    print ('严重肥胖')
