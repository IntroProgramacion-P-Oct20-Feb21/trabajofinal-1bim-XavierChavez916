'''
Solución que imprima el costo de un pedido de un artículo del cual se tiene la 
descripción, la cantidad que se requiere y el precio unitario. Si la cantidad
pedida excede de 50 unidades, se hace un descuento de 15%.
'''
porcentaje = 15
descripción_articulo = input("Ingrese la descripcion del articulo\n> ")
cantidad_pedida = int(input("Ingrese la cantidad que se requiere\n> "))
precio_unitario = float(input("Ingrese el precio unitario del articulo\n> "))

costo_pedido_articulo = cantidad_pedida * precio_unitario

if (cantidad_pedida > 50):
    descuento = (costo_pedido_articulo * porcentaje) / 100
    costo_pedido_articulo = costo_pedido_articulo - descuento

print(f"El nombre del articulo es: {descripción_articulo}\nEl costo es:"
        f" {costo_pedido_articulo:.2f}")