a = 0
b = 1
while a != b:
    entrada = input().split()
    X = int(entrada[0])
    Y = int(entrada[1])
    if X == Y:
        break 
    else:
        if(X > Y) :
            print("Decrescente")
        else:
            print("Crescente")
           
