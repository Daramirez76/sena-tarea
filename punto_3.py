#punto 3
import random
while True:
    try:
        print("------descuento------\n")
        article = input("ingrese el nombre del articulo: ")
        price = int(input("ingrese el precio del articulo: "))
        random_number = random.randint(1,100)

        if random_number < 74:
            offert = price * 0.15
            print(f"\nel articulo seleccionado es: {article}")
            print(f"el precio original del articulo es: {price}")
            print(f"su numero aleatorio es: {random_number}\n")
            print(f"el precio con descuento del articulo es: {offert}")
            
        elif random_number >= 74:
            offert = price * 0.2
            print(f"\nel articulo seleccionado es: {article}")
            print(f"el precio original del articulo es: {price}")
            print(f"su numero aleatorio es: {random_number}\n")
            print(f"el precio con descuento del articulo es: {offert}")
        break

    except ValueError: 
        print("ERROR: ingrese un valor numerico\n")
