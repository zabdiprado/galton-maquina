import matplotlib.pyplot as plt
import random

def simular_galton(canicas, niveles):
    resultados = [0] * (niveles + 1)  # Inicializar contenedores

    # Simular el recorrido de cada canica
    for _ in range(canicas):
        posicion = 0
        for _ in range(niveles):
            posicion += random.choice([-1, 1])  # La canica cae a la izquierda o derecha
        resultados[(niveles + posicion) // 2] += 1  # Registrar la posición final

    return resultados

def graficar_histograma(resultados):
    plt.bar(range(len(resultados)), resultados)
    plt.xlabel("Contenedores")
    plt.ylabel("Cantidad de Canicas")
    plt.title("Distribución de Canicas en la Máquina de Galton")
    plt.show()

# Parámetros de la simulación
canicas = 3000
niveles = 12

# Ejecutar simulación y graficar resultados
resultados = simular_galton(canicas, niveles)
graficar_histograma(resultados)
