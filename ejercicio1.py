billetes = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
billete = input("Introduce una divisa " + "\n")
if billete in billetes:
    print(billetes[billete])
else:
    print("La divisa no se encuentra ")