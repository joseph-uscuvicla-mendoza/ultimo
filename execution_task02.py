# tu codigo aqui
nombre = input("Ingrese su nombre: ")
cantidad_meses = input("Ingrese la cantidad de meses que desea ahorrar: ")
while not cantidad_meses.isdigit() or int(cantidad_meses) > 12:
    print("La cantidad de meses no puede ser mayor a 12")
    cantidad_meses = input("Ingresar la cantidad de meses que desea ahorrar: ")
ahorros_mensuales = []
for i in range(int(cantidad_meses)):
    ahorro_mensual = float(input("Ingrese el ahorro del mes {}: ". format(i+1)))
    ahorros_mensuales.append(ahorro_mensual)
monto_total_ahorro = sum(ahorros_mensuales)
ganancia = monto_total_ahorro * 0.1
print("Nombre:", nombre)
print("Cantidad de meses:", cantidad_meses)
print("Ahorros mensuales:", ahorros_mensuales) 
print("Monto total ahorrando:", monto_total_ahorro)
print("Ganancia:", ganancia)
