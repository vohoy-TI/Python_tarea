#preguntar al usuario la fecha de su nacimiento en el formato 00/00/0000
fecha = input ("ingrese su fecha de nacimiento en el formato dd/mm/aaaa  ")

#separamos las dia de el mes y el anio
partes = fecha.split("/")

#aseguramos el dia y el mes tenga 2 digitos con .zfill(2)
dia = partes[0].zfill(2)
mes = partes[1].zfill(2)
anio = partes[2]

# mostrar en pantalla numero de dia mes y anio
print (f"dia {dia} mes {mes} anio {anio}")

