x = 0
entrada = int(input())

while x < entrada:
    lista = input().split()
    a = float(lista[0])
    b = float(lista[1])
    c = float(lista[2])
    
    media =(((a*2)+(b*3)+(c*5))/10)
    print('%.1f' %media)
    

    x +=1
