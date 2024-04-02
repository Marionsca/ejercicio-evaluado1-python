import math

radio_km = float(input("Por favor, ingresa el radio del planeta en kilómetros: "))

radio_m = radio_km * 1000

g = float(input("Ahora ingresa la constante gravitacional en m/s^2: "))

velocidad_escape = math.sqrt(2 * g * radio_m)

print("La velocidad de escape es:", round(velocidad_escape, 2), "m/s")
 