#Leia 2 valores inteiros X e Y. A seguir, calcule e mostre
#a soma dos números impares entre eles.

x = int(input())
y = int(input())
i = 0

    
if x < y:
    x+= 1
    while x < y:
        if x % 2 != 0:
            i += x
        x += 1
        
if y < x:
    y+= 1
    while y < x:
        if y % 2 != 0:
            i += y
        y += 1
    
print(i)
