entrada = input().split()
inicio = int(entrada[0])
final = int(entrada[1])

hora = 24
# iniciomaior = hr - inicio + final

if inicio > final:
    resultado = hora - inicio + final
    
elif inicio == final:             
     resultado = 24

elif final > inicio:
    resultado = final - inicio



print('O JOGO DUROU %i HORA(S)' %resultado)
