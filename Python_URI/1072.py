

x = 1
y = 0
q = 0

N = int(input())
while N >= x:
    entrada = int(input())
    if entrada >= 10 and entrada <= 20:
        q += 1
        x+=1
    else:
        y += 1
        x+=1
print(q,'in')
print(y,'out')
