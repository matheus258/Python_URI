entrada = input().split()

codigo = int(entrada[0])
quantidade = int(entrada[1])
resp = 0.0

if codigo == 1:
    resp = 4.0 * quantidade
elif codigo == 2:
    resp = 4.5 * quantidade
elif codigo == 3:
    resp = 5.0 * quantidade
elif codigo == 4:
    resp = 2.0 * quantidade
elif codigo == 5:
    resp = 1.5 * quantidade
    
print("Total: R$ %0.2f" %resp) 
