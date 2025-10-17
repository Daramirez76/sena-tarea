#punto 2
while True:
    try: 
        article = input("ingrese el nombre del articulo: ")
        price = int(input("ingrese el precio del articulo: "))
        print("claves:\n1.descuento del 10%\n2.descuento del 20%")
        value = int(input("Selecciones una clave: "))

        if value == 1:
            offert = price * 0.1
            print(f"el articulo seleccionado es: {article}")
            print(f"la clave seleccionada es: {value}")
            print(f"el precio original del articulo es: {price}")
            print(f"el precio con descuento del articulo es: {offert}")
            
        elif value == 2:
            offert = price * 0.2
            print(f"el articulo seleccionado es: {article}")
            print(f"la clave seleccionada es: {value}")
            print(f"el precio original del articulo es: {price}")
            print(f"el precio con descuento del articulo es: {offert}")
        break
            
    except ValueError: 
        print("ERROR: Debe seleccionar una clave valida\n")
