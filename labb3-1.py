# -*- coding: cp1252 -*-
print('Välkommen till den ultimata labb menyn!')
print
print('1: bounce')
print('2: tvärsumma')
print('3: newton-raphson')
print('4: avsluta programmet')



def bounce(stuts):
    if stuts !=0:
        print stuts,
        bounce(stuts-1)
        print stuts,
        return
    else:
        print stuts,

def numsum(n):
    if n > 0:
        n = n % 10 + numsum(n/10)
        k=n

def derivative(f, x, h):
    k =(1.0/(2*h))*(f(x+h)-f(x-h))
    return k

def solve(f, x0, h):
    lastX = x0
    new = 0.0
    while (abs(lastX - new) > h) or lastX==new:
        new = lastX
        lastX = lastX - f(lastX)/derivative(f, lastX, h)
    return lastX

def f(x):
    return x**2-1

def numsum(n):
    if n > 0:
        n = n % 10 + numsum(n/10)
        k=n
    return n
        
loop = 1

while loop ==1:
        print
        val = input('välj vilket programm som ska köras: ')
        val = int(val)
    
        if val == 1:
            stuts = input('mata in talet du vill studsa: ')
            stuts = int(stuts)
            bounce(stuts)
    
        elif val == 2:
            n = input('mata in det tal du vill beräkna tvärsumman av: ')
            print numsum(n)

        elif val == 3:
            x0 = input('mata in startvärdet: ')
            x0 = int(x0)
            h = 0.1
            print solve(f, x0, h)

        elif val == 4:
            loop = 0
        else:
            print('mata in ett värde 1-4.')

