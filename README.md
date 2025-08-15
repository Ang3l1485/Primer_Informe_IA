# Ejercicio #1

## Análisis del problema

El problema consiste en encontrar el camino de menor costo entre dos ciudades en un mapa de Rumania. Este es un problema clásico de búsqueda de la ruta más corta en un grafo ponderado.

Estados: Las ciudades del mapa.

Estado Inicial: Arad.

Estado Objetivo: Bucharest.

Acciones: Moverse de una ciudad a otra ciudad conectada directamente.

Costo de la Acción: La distancia (costo) real de la carretera entre dos ciudades conectadas.

El objetivo es encontrar una secuencia de ciudades (un camino) desde Arad hasta Bucharest tal que la suma de los costos de los tramos individuales sea la mínima posible.


## Aplicación del algoritmo A* (A* Search)

El algoritmo A* Search es una extensión del Best-First Search y evalúa los nodos combinando el costo para llegar al nodo y una estimación del costo restante hasta el objetivo.

1. Definir la Heurística: Se crea un diccionario que mapea cada ciudad a su distancia en línea recta hasta Bucharest.
2. Modificar la Función de Evaluación f(n): Se añade a la función original (que solo usaba g(n)) una nueva parte que suma g(n) y h(n).

## ¿Por qué se considera que la ruta encontrada es óptima?

La ruta encontrada por A* es óptima (garantiza el menor costo) porque utilizamos una heurística admisible.

Una heurística se considera admisible si nunca sobreestima el costo real para llegar al objetivo. Es decir, la estimación siempre es optimista o, en el peor de los casos, exacta.

Nuestra heurística, la distancia en línea recta, es admisible. La razón es simple: la distancia más corta entre dos puntos geográficos es una línea recta. Cualquier ruta por carretera real será, como mínimo, igual de larga que esa línea recta, y usualmente más larga debido a las curvas.

Como A* siempre expande el nodo con el valor f(n) más bajo, y nuestra h(n) es admisible, el algoritmo está garantizado a encontrar la ruta óptima. No dará por finalizada la búsqueda con una solución si existe la posibilidad de que otra ruta, aún no explorada por completo, pueda resultar en un costo total menor.


# Ejercicio #2




