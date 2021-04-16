salario = float(input())

if (salario <= 400.0):
    reajuste = 15
elif (salario <= 800.0):
    reajuste = 12
elif (salario <=1200.0):
     reajuste = 10
elif (salario <2000.0):
    reajuste = 7
else:
    reajuste = 4

print("Novo salario: %.2f" %(salario +(salario * reajuste /100)))
print("Reajuste ganho: %.2f" %(salario * reajuste / 100))
print("Em percentual:",reajuste,"%")
