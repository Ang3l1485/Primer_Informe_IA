# Ejercicio #1

## **Análisis del problema**

El problema consiste en encontrar el camino de menor costo entre dos ciudades en un mapa de Rumania. Este es un problema clásico de búsqueda de la ruta más corta en un grafo ponderado.

Estados: Las ciudades del mapa.

Estado Inicial: Arad.

Estado Objetivo: Bucharest.

Acciones: Moverse de una ciudad a otra ciudad conectada directamente.

Costo de la Acción: La distancia (costo) real de la carretera entre dos ciudades conectadas.

El objetivo es encontrar una secuencia de ciudades (un camino) desde Arad hasta Bucharest tal que la suma de los costos de los tramos individuales sea la mínima posible.


## **Aplicación del algoritmo A\* (A\* Search)**

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

En el código proporcionado, cada movimiento (Arriba, Abajo, Izquierda, Derecha) tiene un costo uniforme de **1**. Esto significa que el algoritmo encuentra el **camino más corto** en términos del número de pasos.

Si introdujeras diferentes costos para atravesar diferentes tipos de terreno (por ejemplo, moverse a través de una celda de "agua" cuesta 3, mientras que una celda de "camino" cuesta 1), el comportamiento del algoritmo cambiaría. En lugar de simplemente encontrar el camino con la menor cantidad de celdas, priorizaría rutas que, aunque potencialmente más largas en distancia, tuvieran un costo acumulado menor. El algoritmo favorecería los caminos con más celdas de "camino", incluso si eso significara tomar una ruta más larga para evitar las celdas de "agua" de mayor costo.

---

## **¿Qué sucede si hay múltiples salidas en el laberinto y cómo se podría modificar el algoritmo?**

Actualmente, el algoritmo está diseñado con un único estado objetivo (la salida 'E') que se detecta al inicio. Si el laberinto tuviera múltiples salidas, el programa solo encontraría la primera que identifique y no sería consciente de las demás.

Para manejar múltiples salidas, se podría implementar las siguientes modificaciones:

* **Definir Múltiples Objetivos:** En lugar de un único `goal_state`, define una lista o conjunto con las coordenadas de todas las salidas posibles.
* **Actualizar la Verificación del Objetivo:** Modifica la condición de parada del bucle principal para comprobar si el estado actual está presente en el conjunto de estados objetivo.
* **Ajustar la Heurística:** La función heurística (por ejemplo, la distancia de Manhattan) debe actualizarse para calcular la distancia a la salida *más cercana* desde la posición actual. Esto asegura que la heurística siga siendo admisible (nunca sobreestima el costo real), lo cual es crucial para que A\* garantice encontrar el camino óptimo.

Con estos cambios, el algoritmo encontraría de manera eficiente el camino óptimo hacia la salida que sea más cercana o más barata de alcanzar desde el punto de partida.

---

## **Modifica el laberinto y encuentra una limitación en el algoritmo.**

El siguiente ejemplo muestra un laberinto diferente. 'W' para "Agua", que es transitable pero tiene un costo de movimiento mayor (por ejemplo, un costo de 3).

```python
# Laberinto modificado con un nuevo obstáculo 'W' (Agua)
large_maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", " ", " ", "#", "W", "W", " ", " ", " ", "E", "#"],
    ["#", " ", "#", " ", "#", "W", " ", "#", "#", " ", "#", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]
```
El principal limitante del algoritmo A\* proporcionado es que asume un costo uniforme para cada movimiento. La línea new_cost = current_node.path_cost + 1 fija un costo de movimiento de 1 para cualquier casilla válida, lo que lo hace incapaz de calcular correctamente el costo del camino cuando se introducen terrenos con diferentes costos, como el agua ('W'). El algoritmo encontrará el camino con menos pasos, pero no necesariamente el de menor costo real.

# Ejercicio #3

## **Comparación de Resultados**

Al ejecutar ambos algoritmos para encontrar la ruta de la **Estación A** a la **Estación J**, ambos encuentran la misma ruta óptima. Sin embargo, los datos de rendimiento que proporcionaste revelan las diferencias clave en su eficiencia.

| Métrica | Breadth-First Search (BFS) | Iterative Deepening Search (IDS) |
| :--- | :--- | :--- |
| **Ruta de Solución** | `['A', 'C', 'F', 'J']` | `['A', 'C', 'F', 'J']` |
| **Pasos** | 3 | 3 |
| **Tiempo de Ejecución**| 0.076 ms | **0.068 ms** |
| **Memoria Pico** | 6.1 KiB | **3.523 KiB** |

**Observación Clave:** Los resultados confirman la teoría. **IDS utiliza significativamente menos memoria** (casi la mitad) que BFS. Aunque teóricamente IDS suele ser un poco más lento por re-explorar nodos, en este caso específico y con un grafo tan pequeño, ha resultado ser marginalmente más rápido. Esto puede deberse a la eficiencia de la implementación o al bajo costo de la re-exploración en este escenario.

---

### **Explicación de las Diferencias Encontradas**

Las diferencias en rendimiento se deben a la estrategia fundamental de cada algoritmo para explorar el grafo de estaciones.

#### **Breadth-First Search (BFS) **

BFS explora la red "capa por capa", asegurando encontrar la ruta más corta.

* **Estrategia:** Empieza en A, luego visita a todos sus vecinos (B, C), luego a los vecinos de estos (D, E, F), y así sucesivamente. Para lograrlo, debe mantener una lista (la "frontera") de todas las estaciones que ha descubierto pero cuyos vecinos aún no ha explorado.
* **Ventaja - Tiempo:** Es muy eficiente en tiempo porque visita cada estación una sola vez.
* **Desventaja - Memoria:** Su gran debilidad es la memoria. La "frontera" de nodos puede crecer exponencialmente. En tu ejecución, necesitó **6.1 KiB** para almacenar estas listas, lo cual es considerablemente más que IDS. Para un mapa de metro con miles de estaciones, BFS podría agotar la memoria del sistema.

#### **Iterative Deepening Search (IDS) 💡**

IDS combina lo mejor de la búsqueda en profundidad (bajo uso de memoria) y la búsqueda en anchura (encontrar la ruta más corta).

* **Estrategia:** Realiza múltiples búsquedas en profundidad con un límite que va incrementando: primero busca rutas de 1 paso, luego de 2, y finalmente de 3 pasos, donde encuentra la solución.
* **Ventaja - Memoria:** ¡Su punto fuerte es el ahorro de memoria! Solo necesita recordar la ruta actual que está explorando (ej: A -> C -> F). Como demostró tu ejecución, solo necesitó **3.523 KiB**. Esta característica lo hace ideal para problemas con un espacio de estados enorme.
* **Desventaja - Tiempo:** Su debilidad teórica es que re-explora los nodos de niveles superiores en cada nueva iteración. Por ejemplo, para buscar a profundidad 3, vuelve a recorrer las rutas de profundidad 1 y 2. Aunque esto lo hace potencialmente más lento, tus resultados muestran que para este problema tan pequeño, este costo fue insignificante e incluso resultó ser un poco más rápido.


