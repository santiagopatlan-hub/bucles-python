num = int(input("numero para factorial: "))
factorial = 1

if num < 0:
    print("factorial no definido para negativos")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("el factorial de", num, "es:", factorial)