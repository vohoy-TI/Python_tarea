#pedir al usuario el precio del producto en euros y centimos
precio = input("ingrese el precio en euros con dos decimales(0.00)")

#dividir en partes y extraerlas a las vaiables euros y centimos
euros, centimos = precio.split(".")

#mostrar en pantalla la cantidad de euros y la cantidad de centimos 
print (f"su producto cuesta {euros} euros y {centimos} centimos")
