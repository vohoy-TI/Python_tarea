#pedir el numero de telefono con prefijo y extencuion separado por guion (-)
numero_completo = input("ingrese el prefijo, su numero y extencion separado por un guion (000-00000-0000)")

#dividir el numero en partes 
partes = numero_completo.split("-")

#exptaer la segunda parte del numero_completo
solo_numero = partes[1]

#mostrar en pantalla
print(f"el numero sin prefijo ni extencion es {solo_numero}")
