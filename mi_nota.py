# Abro el archivo en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    print("Contenido de my_notes.txt:")
    
    # Leo la primera línea
    line = file.readline()
    while line != '':  # Mientras no llegue al final del archivo
        print(line.strip())  # Muestro la línea sin el salto de línea final
        line = file.readline()  # Leo la siguiente línea
        
# El archivo se cierra automáticamente al salir del bloque 'with'