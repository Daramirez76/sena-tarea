#punto 4
ventas = []
for i in range(1, 101):
    while True:
        try:
            venta = float(input(f"Ingrese la venta anual del vendedor {i}: "))
            if 1000000 <= venta < 10000000:
                ventas.append(venta)
                break
            else:
                print("ERROR: La venta debe estar entre 1,000,000 y 10,000,000")
        except ValueError:
            print("ERROR: Ingrese un valor numérico válido")

for i, venta in enumerate(ventas, start=1):
    if 1000000 <= venta < 3000000:
        comision = venta * 0.03
    elif 3000000 <= venta < 5000000:
        comision = venta * 0.04
    elif 5000000 <= venta < 7000000:
        comision = venta * 0.05
    elif 7000000 <= venta < 10000000:
        comision = venta * 0.06
    
    print(f"Vendedor {i}: Venta = {venta}, Comisión = {comision}")
