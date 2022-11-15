nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")
direccion = input("¿Donde vives? ")
telefono = input("¿Cual es tu numero de teléfono? ")
usuario = {"nombre":nombre, "edad":edad, "direccion":direccion, "telefono":telefono}
print(usuario["nombre"], "tiene", usuario["edad"], "años, vive en", usuario["direccion"], "y su número de telefono es", usuario["telefono"])