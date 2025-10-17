#punto 1
while True:
    try:
        number = float(input("Ingrese un número: "))

        if number < 0:
            valor_absoluto = number * -1
        else:
            valor_absoluto = number

        print(f"El valor absoluto de {number} es: {valor_absoluto}")
        break

    except ValueError:
        print("ERROR: Ingrese un valor numérico válido\n")

































