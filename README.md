# Ejercicio #1

## **Análisis del problema**

El problema consiste en encontrar el camino de menor costo entre dos ciudades en un mapa de Rumania. Este es un problema clásico de búsqueda de la ruta más corta en un grafo ponderado.

Estados: Las ciudades del mapa.

Estado Inicial: Arad.

Estado Objetivo: Bucharest.

Acciones: Moverse de una ciudad a otra ciudad conectada directamente.

Costo de la Acción: La distancia (costo) real de la carretera entre dos ciudades conectadas.

El objetivo es encontrar una secuencia de ciudades (un camino) desde Arad hasta Bucharest tal que la suma de los costos de los tramos individuales sea la mínima posible.


## **Aplicación del algoritmo A* (A* Search)**

El algoritmo A* Search es una extensión del Best-First Search y evalúa los nodos combinando el costo para llegar al nodo y una estimación del costo restante hasta el objetivo.

1. Definir la Heurística: Se crea un diccionario que mapea cada ciudad a su distancia en línea recta hasta Bucharest.
2. Modificar la Función de Evaluación f(n): Se añade a la función original (que solo usaba g(n)) una nueva parte que suma g(n) y h(n).

## **¿Por qué se considera que la ruta encontrada es óptima?**

La ruta encontrada por A* es óptima (garantiza el menor costo) porque utilizamos una heurística admisible.

Una heurística se considera admisible si nunca sobreestima el costo real para llegar al objetivo. Es decir, la estimación siempre es optimista o, en el peor de los casos, exacta.

Nuestra heurística, la distancia en línea recta, es admisible. La razón es simple: la distancia más corta entre dos puntos geográficos es una línea recta. Cualquier ruta por carretera real será, como mínimo, igual de larga que esa línea recta, y usualmente más larga debido a las curvas.

Como A* siempre expande el nodo con el valor f(n) más bajo, y nuestra h(n) es admisible, el algoritmo está garantizado a encontrar la ruta óptima. No dará por finalizada la búsqueda con una solución si existe la posibilidad de que otra ruta, aún no explorada por completo, pueda resultar en un costo total menor.


# Ejercicio #2

## **¿Cómo cambia el comportamiento del algoritmo si cambiamos la función de costo?**

Cambiar la función de costo altera fundamentalmente la definición del "mejor" camino. El algoritmo actual, A\*, busca encontrar la ruta con el costo total más bajo.

En el código proporcionado, cada movimiento (Arriba, Abajo, Izquierda, Derecha) tiene un costo uniforme de **1**[cite: 60]. Esto significa que el algoritmo encuentra el **camino más corto** en términos del número de pasos.

Si introdujeras diferentes costos para atravesar diferentes tipos de terreno (por ejemplo, moverse a través de una celda de "agua" cuesta 3, mientras que una celda de "camino" cuesta 1), el comportamiento del algoritmo cambiaría. En lugar de simplemente encontrar el camino con la menor cantidad de celdas, priorizaría rutas que, aunque potencialmente más largas en distancia, tuvieran un costo acumulado menor. El algoritmo favorecería los caminos con más celdas de "camino", incluso si eso significara tomar una ruta más larga para evitar las celdas de "agua" de mayor costo.

---

## **¿Qué sucede si hay múltiples salidas en el laberinto y cómo se podría modificar el algoritmo?**

Actualmente, el algoritmo está diseñado con un único estado objetivo (la salida 'E') que se detecta al inicio. Si el laberinto tuviera múltiples salidas, el programa solo encontraría la primera que identifique y no sería consciente de las demás.

Para manejar múltiples salidas, podrías implementar las siguientes modificaciones[cite: 54, 55]:

* [cite_start]**Definir Múltiples Objetivos:** En lugar de un único `goal_state`, define una lista o conjunto con las coordenadas de todas las salidas posibles[cite: 54, 55].
* [cite_start]**Actualizar la Verificación del Objetivo:** Modifica la condición de parada del bucle principal para comprobar si el estado actual está presente en el conjunto de estados objetivo[cite: 54, 55].
* **Ajustar la Heurística:** La función heurística (por ejemplo, la distancia de Manhattan) debe actualizarse para calcular la distancia a la salida *más cercana* desde la posición actual. Esto asegura que la heurística siga siendo admisible (nunca sobreestima el costo real), lo cual es crucial para que A\* garantice encontrar el camino óptimo.

Con estos cambios, el algoritmo encontraría de manera eficiente el camino óptimo hacia la salida que sea más cercana o más barata de alcanzar desde el punto de partida.

---

## **Modifica el laberinto y encuentra una limitación en el algoritmo.**

[cite_start]Aquí tienes un ejemplo de un laberinto más grande con un nuevo obstáculo, 'W' para "Agua", que es transitable pero tiene un costo de movimiento mayor (por ejemplo, un costo de 3)[cite: 55].

```python
# Laberinto modificado con un nuevo obstáculo 'W' (Agua)
large_maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", " ", " ", "#", "W", "W", " ", " ", " ", "E", "#"],
    ["#", " ", "#", " ", "#", "W", " ", "#", "#", " ", "#", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]