entrada = int(input())
x = 1

while x <= 10000:
    while x % entrada == 2:
        print(x)
        x+=1
    x+=1
