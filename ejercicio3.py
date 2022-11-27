productos = {"Pan":1.40, "Huevos":2.30, "Cebolla":0.85, "Aceite":4.33}
producto = input("¿Qué producto quieres? ")
if producto not in productos:
    print("Lo siento este producto no tenemos")
else:
    numero_unidades = float(input("¿Cuántas unidades quieres? "))
    print(numero_unidades, "unidades de", producto, "valen", productos[producto] * numero_unidades, "€")

