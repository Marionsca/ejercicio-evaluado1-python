P_normal = float(input("Ingrese el precio de suscripción para usuarios normales: "))
U_normal = int(input("Ingrese el número de usuarios normales: "))
P_premium = 1.5 * P_normal  # Precio de suscripción para usuarios premium
U_premium = int(input("Ingrese el número de usuarios premium: "))
GT = float(input("Ingrese los gastos totales: "))

utilidades = (P_normal * U_normal + P_premium * U_premium) - GT

print("Las utilidades del proyecto son:", utilidades)
