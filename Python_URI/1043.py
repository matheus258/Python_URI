entrada = input().split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

perimetro = A+B+C
area = ((A+B)*C/2)

if A + B > C and A + C > B and B + C > A:
    print("Perimetro = %.1f" % perimetro)

else:
    print("Area = %.1f" %area)
