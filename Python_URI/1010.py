#C1 = int(input())
#N1 = int(input())
#V1 = float(input())

#C2 = int(input())
#N2 = int(input())
#V2 = float(input())

#soma1 = N1 * V1
#soma2 = N2 * V2
#resultado = soma1 + soma2

#print('VALOR A PAGAR: R$ %.2f' % resultado)


linha = input().split()
C1 = int(linha[0])
N1 = int(linha[1])
V1 = float(linha[2])

linha2 = input().split()
C2 = int(linha2[0])
N2 = int(linha2[1])
V2 = float(linha2[2])

resultado = N1 * V1 + N2 * V2
print('VALOR A PAGAR: R$ %.2f' % resultado)
