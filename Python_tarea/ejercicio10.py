

productos = input(" ingrese los productos de la cesta separado por coma(producto1,producto2,producto3)")


producto_individual = productos.split(",")

print (" los productos de la cesta son: ")
for producto in producto_individual:

    print (f"{producto}") 
