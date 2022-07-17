# Escribir una función que calcule el total de una 
# factura tras aplicarle el IVA. La función debe 
# recibir la cantidad sin IVA y el porcentaje de 
# IVA a aplicar, y devolver el total de la factura.

# registros_de_iva.txt
# subtotal, el porcentaje aplicado, y el total
# 100, 21, 121


def guardar_importes(valor: int, porcentaje: int, valor_final: int):
    archivo = open("./registros_de_iva.txt", "a")

    archivo.write(f"{valor},{porcentaje},{valor_final}\n")
    archivo.close()


def calcular_iva(valor, porcentaje):

    valor_final = valor + ( valor * porcentaje / 100)

    # Invocar a la funcion de guardado
    guardar_importes(valor, porcentaje, valor_final)

    return valor_final


importe = int(input("Ingrese el importe neto: "))
porcentaje = int(input("Ingrese el porcentaje: "))

importe_total = calcular_iva(importe, porcentaje)
print(f"El usuario debe abonar ${importe_total}")
