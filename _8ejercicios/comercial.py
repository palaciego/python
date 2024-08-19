'''EL COMERCIAL: 
Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un 
programa para realizar un seguimiento de los productos que has vendido y el valor total de las 
ventas. Supongamos que hay un total de 10 productos.  
Tú has vendido 5 de estos productos en las siguientes cantidades: 
producto1: 3 unidades 
producto2: 1 unidad 
producto5: 7 unidades 
producto6: 2 unidades 
producto9 : 4 unidades 
Los precios de cada uno de estos productos son como siguen: 
Producto 1: 30.0 EU		
Producto 2: 9.8 EU		
Producto 3: 42.5 EU		
Producto 4: 32.6 EU		
Producto 5: 71.5 EU		
Producto 6: 44.0 EU	 
Producto 7: 21.2 EU 
Producto 8: 53.2 EU 
Producto 9: 25.3 EU 
Producto 10: 57.8 EU 
Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima 
la cantidad total de ventas, el dinero facturado por productoy el dinero total. '''

# Datos de los productos y sus precios
bruto = """
Producto 1: 30.0 EU        
Producto 2: 9.8 EU        
Producto 3: 42.5 EU        
Producto 4: 32.6 EU        
Producto 5: 71.5 EU        
Producto 6: 44.0 EU     
Producto 7: 21.2 EU 
Producto 8: 53.2 EU 
Producto 9: 25.3 EU 
Producto 10: 57.8 EU
"""

# Datos de las ventas realizadas
ventas = {
    "Producto 1": 3,
    "Producto 2": 1,
    "Producto 5": 7,
    "Producto 6": 2,
    "Producto 9": 4
}

def comercial():
    dic = {}
    # --- Lista productos/precio ---
    lines = bruto.strip().split("\n")
    for line in lines:
        producto, precio = line.split(":")
        precio = float(precio.strip().replace(" EU", ""))
        dic[producto.strip()] = precio
    return dic

# Llamar a la función para obtener el diccionario de productos y precios
productos_precios = comercial()

# Calcular el total de ventas y el dinero facturado por producto
total_ventas = 0
total_dinero = 0.0

print("Detalle de ventas:")
for producto, unidades_vendidas in ventas.items():
    precio = productos_precios[producto]
    dinero_facturado = precio * unidades_vendidas
    total_ventas += unidades_vendidas
    total_dinero += dinero_facturado
    print(f"{producto}: {unidades_vendidas} unidades, {dinero_facturado:.2f} EU")

print("\nResumen:")
print(f"Total de unidades vendidas: {total_ventas}")
print(f"Dinero total facturado: {total_dinero:.2f} EU")
