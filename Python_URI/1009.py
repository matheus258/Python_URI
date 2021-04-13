nome = input()
salario = float(input())
vendas = float(input())
cm = vendas * 0.15
salario = cm + salario
print('TOTAL = R$ %.2f' % salario)
