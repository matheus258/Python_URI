par = 0

a = int(input())
resultado = a % 2
if resultado == 0:
    par = par + 1
    
b = int(input())
resultado = b % 2
if resultado == 0:
    par = par + 1
    
c = int(input())
resultado = c % 2
if resultado == 0:
    par = par + 1
    
d = int(input())
resultado = d % 2
if resultado == 0:
    par = par + 1
    
e = int(input())
resultado = e % 2
if resultado == 0:
    par = par + 1

print (par,"valores pares")
