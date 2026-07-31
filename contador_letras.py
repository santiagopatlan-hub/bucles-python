palabra = input("ingrese una palabra: ").lower()
contador = 0

for letra in palabra:
    if letra == 'a':
        contador += 1

print("aa letra 'a' aparece", contador, "veces")