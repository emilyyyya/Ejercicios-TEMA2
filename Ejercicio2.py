def modificar(lista):
    # Eliminar duplicados y ordenar de mayor a menor en un solo paso
    lista_unica = sorted(set(lista), reverse=True)
    
    # Filtrar números pares
    lista_pares = [num for num in lista_unica if num % 2 == 0]
    
    # Calcular la suma de los números pares
    suma = sum(lista_pares)
    
    # Crear la nueva lista con la suma al principio
    lista_modificada = [suma] + lista_pares
    
    return lista_modificada

# Solicitar al usuario que ingrese los números de la lista
entrada = input("Introduce los números de la lista, separados por comas: ")
lista = [int(x) for x in entrada.split(",")]

# Llamar a la función modificar
nueva_lista = modificar(lista)

# Comprobación
print(nueva_lista)
print(nueva_lista[0] == sum(nueva_lista[1:]))  # Debe imprimir True si la suma es correcta
