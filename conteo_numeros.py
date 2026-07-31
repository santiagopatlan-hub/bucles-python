n = int(input("cantidad de números a ingresar: "))
mayores = 0
menores = 0
iguales = 0

for i in range(n):
    num = int(input("numero: "))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales += 1

print("mayores a 0:", mayores)
print("menores a 0:", menores)
print("iguales a 0:", iguales)