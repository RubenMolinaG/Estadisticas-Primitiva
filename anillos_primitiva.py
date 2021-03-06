import matplotlib.pyplot as plt

# Creación de la matriz.
def creacion_matriz_primitiva() -> list:
    matriz = []
    for k in range(10):
        vector = []
        for numero in range(k, (50+k), 10):
            if numero != 0:
                vector.append(numero)
        matriz.append(vector)
    return matriz

# Pintamos la matriz.
def pintar_matriz(matriz: list):
    for vector in matriz:
        print("")
        for numero in vector:
            print(numero, end="\t")
    print("\n")

# Vector con los numeros del anillo externo.
def vector_anillo_externo(matriz: list) -> list:
    vector = []
    for numero in matriz[0]:
        vector.append(numero)
    for numero in matriz[len(matriz) - 1]:
        vector.append(numero)
    for numero in range(1, 9):
        vector.append(numero)
    for numero in range(41, 49):
        vector.append(numero)
    return vector

# Vector con los numeros del anillo medio.
def vector_anillo_medio() -> list:
    vector = []
    for numero in range(11, 19):
        vector.append(numero)
    for numero in range(31, 39):
        vector.append(numero)
    vector.append(21)
    vector.append(28)
    return vector

# Vector con los numeros del anillo interno.
def vector_anillo_interno() -> list:
    vector = []
    for numero in range(22, 28):
        vector.append(numero)
    return vector

# Crear un diccionario con los elementos del anillo pasado por argumento:
def crear_diccionario(vector: list) -> dict():
    diccionario = {}
    for numero in vector:
        diccionario[numero] = 0
    return diccionario

# Rellenar los diccionarios:
def rellenar_diccionarios(diccionario: dict):
    for linea in open('./data/historico_numero_apariciones.csv', 'r'):
        linea   = linea.split(',')
        numero  = int(linea[0])
        repeticiones = int(linea[1])
        if numero in diccionario.keys():
            diccionario[numero] = repeticiones
    return diccionario

# Dibujar la gráfica de los 3 diccionarios:
def dibujar_grafica(anillo_externo: dict, anillo_medio: dict, anillo_interno: dict):
    
    plt.scatter(anillo_externo.keys(), anillo_externo.values())
    plt.scatter(anillo_medio.keys(), anillo_medio.values())
    plt.scatter(anillo_interno.keys(), anillo_interno.values())
    plt.xticks(list(range(1, 50)))

    plt.grid('on')
    plt.title('Estadísticas Anillos Primitiva.')
    plt.xlabel('Numeros')
    plt.ylabel('Apariciones')
    plt.legend(['Anillo Exterior', 'Anillo Medio', 'Anillo Interior'])
    plt.show()

# Dibujar la gráfica del porcentaje de aparición de cada uno de los anillos:
def dibujar_grafica_porcentaje(anillo_externo: int, anillo_medio: int, anillo_interno: int):
    plt.bar('Anillo Externo', anillo_externo)
    plt.bar('Anillo Medio', anillo_medio)
    plt.bar('Anillo Interno', anillo_interno)
    plt.yticks(list(range(0, 100, 5)))

    plt.title('% de Aparición Números de cada Anillo.')
    plt.ylabel('% de Aparición')
    plt.grid('on')

    plt.show()

# Función Principal:
def main():

    # Creamos la matriz:
    matriz = creacion_matriz_primitiva()

    # Creación de los vectores:
    v_anillo_externo, v_anillo_medio, v_anillo_interno = vector_anillo_externo(matriz), vector_anillo_medio(), vector_anillo_interno()
    
    # Creacion de los diccionarios:
    diccionario_anillo_externo, diccionario_anillo_medio, diccionario_anillo_interno  = crear_diccionario(v_anillo_externo), crear_diccionario(v_anillo_medio), crear_diccionario(v_anillo_interno)
     
    #Relleno de los diccionarios:
    diccionario_anillo_externo  = rellenar_diccionarios(diccionario_anillo_externo)
    diccionario_anillo_medio    = rellenar_diccionarios(diccionario_anillo_medio)
    diccionario_anillo_interno  = rellenar_diccionarios(diccionario_anillo_interno)
    
    # Dibujamos la gráfica:
    #dibujar_grafica(diccionario_anillo_externo, diccionario_anillo_medio, diccionario_anillo_interno)

    # Calculamos los porcentajes de aparición de cada uno de los anillos:
    total_anillo_externo, total_anillo_medio, total_anillo_interno, total_general = 0, 0, 0, 0
    for apariciones in diccionario_anillo_externo.values():
        total_anillo_externo += apariciones
        total_general += apariciones
    for apariciones in diccionario_anillo_medio.values():
        total_anillo_medio += apariciones
        total_general += apariciones
    for apariciones in diccionario_anillo_interno.values():
        total_anillo_interno += apariciones
        total_general += apariciones

    porcentaje_anillo_externo   = round((total_anillo_externo * 100 / total_general), 2)
    porcentaje_anillo_medio     = round((total_anillo_medio * 100 / total_general), 2)
    porcentaje_anillo_interno   = round((total_anillo_interno * 100 / total_general), 2)

    # Dibujamos la gráfica con los porcentajes:
    dibujar_grafica_porcentaje(porcentaje_anillo_externo, porcentaje_anillo_medio, porcentaje_anillo_interno)

    
if __name__ == '__main__':
    main()
