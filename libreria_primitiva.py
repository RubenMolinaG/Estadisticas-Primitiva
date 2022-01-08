import matplotlib.pyplot as plt

# Crear un diccionario vacio con los números del 1 al 49.
def crear_diccionario() -> dict:
    diccionario = {}
    for number in range(1, 50):
        diccionario[str(number)] = 0
    return diccionario

# Ordenar el diccionario por su valor.
def ordenar_diccionario(diccionario: dict) -> dict:
    return {k: v for k, v in sorted(diccionario.items(), key=lambda item: item[1], reverse=True)}

# Dibuja la gráfica del diccionario que se le pase como argumento.
def dibujar_grafica(diccionario: dict) -> None:
    x_data = diccionario.keys()
    y_data = diccionario.values()
    
    plt.scatter(x_data, y_data, color='yellowgreen')
    plt.title('Estadísticas Primitiva.', fontweight='bold')
    plt.xlabel('$\it{Numeros.}$')
    plt.ylabel('$\it{Repetición.}$')
    plt.grid('on')
    plt.show()

# Dibujar a gráfica como Plot.
def dibujar_grafica_plot(diccionario: dict) -> None:
    x_data = diccionario.keys()
    y_data = diccionario.values()
    
    plt.plot(x_data, y_data, 'bo--')
    plt.title('Estadísticas Primitiva.', fontweight='bold')
    plt.xlabel('$\it{Numeros.}$')
    plt.ylabel('$\it{Repetición.}$')
    plt.grid('on')
    plt.show()

# Crear un fichero JSON de los datos en CSV.
def crear_fichero_json():
    pass
 