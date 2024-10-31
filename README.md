# Simulación de Máquina de Galton en Python

Este proyecto simula una **máquina de Galton** con 3000 canicas y 12 niveles de obstáculos. La simulación calcula la distribución de las canicas en los contenedores finales y muestra un histograma que representa dicha distribución.

## Descripción

La máquina de Galton es un experimento de probabilidad en el cual las canicas caen a través de una serie de obstáculos, dirigiéndose aleatoriamente hacia la izquierda o la derecha en cada nivel. Esto da lugar a una distribución que se asemeja a una curva normal en los contenedores finales. Este programa utiliza Python para simular el recorrido de las canicas y representar el resultado mediante un histograma.

## Proceso de Desarrollo

Para la creación de este código, seguimos estos pasos:

1. **Definición del problema**: El objetivo fue simular el recorrido de 3000 canicas a través de 12 niveles de obstáculos, donde cada canica se desvía aleatoriamente hacia un lado en cada nivel.

2. **Diseño de la solución**:
   - Decidimos dividir el programa en dos funciones:
      - **`simular_galton`** para calcular el resultado del recorrido de cada canica.
      - **`graficar_histograma`** para mostrar los resultados en un histograma.

3. **Implementación de la función `simular_galton`**:
   - Creamos un arreglo para representar los contenedores de las canicas.
   - Simulamos el trayecto de cada canica generando movimientos aleatorios (izquierda o derecha) en cada nivel y calculamos su posición final en el contenedor correspondiente.

4. **Implementación de la función `graficar_histograma`**:
   - Utilizamos `matplotlib` para graficar los resultados en un histograma, agregando etiquetas en los ejes y un título para describir la distribución de las canicas.

5. **Pruebas y ajustes**:
   - Probamos el programa para verificar que la simulación produjera una distribución adecuada y que el histograma reflejara los resultados esperados.

## Requisitos

- **Python** 3.6 o superior
- **matplotlib** (para instalarlo, sigue los pasos en la sección de Instalación)

## Instalación

1. Clona el repositorio o descarga los archivos del proyecto.
2. Abre una terminal en la carpeta del proyecto.
3. Instala el módulo `matplotlib` ejecutando el siguiente comando:

   ```bash
   pip install matplotlib

 
