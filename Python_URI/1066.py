par = 0
impar = 0
positivo = 0
negativo = 0

a = int(input())
resultado = a % 2
if resultado == 0:
    par = par + 1
else:
    impar += 1

if a > 0:
    positivo += 1
elif a < 0:
    
    negativo += 1
    
b = int(input())
resultado = b % 2
if resultado == 0:
    par = par + 1
else:
    impar += 1

if b > 0:
    positivo += 1
elif b < 0:
    negativo += 1
    
c = int(input())
resultado = c % 2
if resultado == 0:
    par = par + 1
else:
    impar += 1

if c > 0:
    positivo += 1
elif c < 0:
    negativo += 1
    
d = int(input())
resultado = d % 2
if resultado == 0:
    par = par + 1
else:
    impar += 1

if d > 0:
    positivo += 1
elif d < 0:
    negativo += 1
    
e = int(input())
resultado = e % 2
if resultado == 0:
    par = par + 1
else:
    impar += 1

if e > 0:
    positivo += 1
elif e < 0:
    negativo += 1

print(par,"valor(es) par(es)")
print(impar,"valor(es) impar(es)")
print(positivo,"valor(es) positivo(s)")
print(negativo,"valor(es) negativo(s)")
