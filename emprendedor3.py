P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese los gastos totales: "))
U_anterior = float(input("Ingrese las utilidades del año anterior: "))

utilidades = P * U - GT

razon_utilidades = utilidades / U_anterior

print("Las utilidades del proyecto son:", utilidades)
print("La razón entre las utilidades actuales y las del año anterior es: {:.2f}".format(razon_utilidades))
