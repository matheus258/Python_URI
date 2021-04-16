map =input().split()

x = float(map[0])
y = float(map[1])

if x == 0 and y == 0:
    #valor = Origem
    print("Origem")

elif x > 0 and y > 0:
   # valor = Q1
    print("Q1")

elif x < 0 and y > 0:
   # valor = Q2
    print("Q2")

elif x> 0 and y <0:
    #valor = Q4
    print("Q4")

elif x <0 and y < 0:
    #valor = Q3
#else:  
    print("Q3")
elif y == 0 and x < 0 or x > 0:
    print("Eixo X")

elif x == 0 and y >0 or y< 0:
    print("Eixo Y")
