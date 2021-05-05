numeros = int(input())

x = 1

while numeros >= x:
    entrada = int(input())
    
    if entrada % 2 == 0 and entrada > 0:
        x+=1
        print('EVEN POSITIVE')
        
    if entrada % 2 == 0 and entrada < 0:
        x+=1
        print('EVEN NEGATIVE')
        
    if entrada % 2 != 0 and entrada > 0:
        x+=1
        print('ODD POSITIVE')
        
    if entrada % 2 != 0 and entrada < 0:
        x+=1
        print('ODD NEGATIVE')
    

    if entrada == 0:
        print('NULL')
        x+=1
