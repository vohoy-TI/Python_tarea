#preguntar el nombre al asuario
nombre = input("¿cómo te llamas?")

#combertir el nombre en mayusculas
nombre_mayusculas = nombre.upper()

#contar las letras
letras = len(nombre.replace(" "," "))

#mostrar el resultado por pantalla
print(f"{nombre_mayusculas} tiene {letras} letras")

