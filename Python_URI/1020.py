quantidaDias = int(input())

qAnos = quantidaDias//365
resto = quantidaDias%365

qmeses = resto//30
dias = resto%30

print(str(qAnos)+' ano(s)')
print(str(qmeses)+' mes(es)')
print(str(dias)+' dia(s)')

