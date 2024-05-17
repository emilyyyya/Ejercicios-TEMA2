# Texto original
texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

# Separar el texto en líneas
lineas = texto.split('#')

# Crear una lista para almacenar las líneas transformadas
lineas_transformadas = []

# Capitalizar la primera línea y añadir puntos suspensivos
lineas_transformadas.append(lineas[0].capitalize() + "...")

# Formatear y capitalizar las líneas de diálogo
for linea in lineas[1:]:
    linea_transformada = "- " + linea[0].upper() + linea[1:] + "."
    lineas_transformadas.append(linea_transformada)

# Unir las líneas transformadas en un único texto con saltos de línea
texto_transformado = "\n\n".join(lineas_transformadas)

print(texto_transformado)
