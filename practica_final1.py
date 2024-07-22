euro_a_mxn = 23.70
usd_a_mxn = 20.75

tipo_de_conversion = input ("Ingrese la moneda origen para la conversion(EUR/USD): ").lower()
monto_a_convertir = float(input ("Ingrese el monto a convertir: "))

if tipo_de_conversion == "eur":
    resultado1 = monto_a_convertir*euro_a_mxn
    print (f"El resultado de la conversion de EURO A PESO MEJICANO ES: {resultado1}")

elif tipo_de_conversion == "usd":
    resultado2 = monto_a_convertir*usd_a_mxn
    print(f"El resultado de la conversion de DOLAR A PESO MEJICANO ES: {resultado2}")

else:
    print("EL TIPO DE CONVERSION SOLICITADO NO ESTA DISPONIBLE")
