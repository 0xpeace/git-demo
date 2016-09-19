#用递归解决汉诺塔移动代码部分
#coding:utf-8
def move(n,a,b,c):
    if n==1:
        print(a'-->'c)
        return
    else:
        move(n-1,A,C,B)
        move(1,A,B,C)
        move(n-1,B,A,C)
    
