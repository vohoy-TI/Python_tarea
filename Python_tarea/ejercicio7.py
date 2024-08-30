#pedir al usuario una direccion de correo
correo = input(" ingrese su correo electronico: ")

#vividir en partes
partes = correo.split("@")

#expraer las partes
direccion = partes[0]

#mostrar en pantalla la direccion modificada
print(f" {direccion }@.ceu.es ")
