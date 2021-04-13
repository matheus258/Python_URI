segundos = int(input())

horas = segundos // 3600
resto = segundos%3600

minutos = resto//60
s = resto%60
print(str(horas)+":"+str(minutos)+":"+str(s))
