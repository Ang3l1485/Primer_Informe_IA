# Ejercicio de las estaciones del metro utilizando el algoritmo BFS (Best-First Search)
import heapq #El módulo heapq para implementar colas de prioridad (heaps)
import tracemalloc
from time import perf_counter
#Definimos las estaciones cómo nodos

class Node: #definición de clase node
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state #El estado que define el nodo
        self.parent = parent #El nodo padre de donde se origina el nodo actual
        self.action = action #Action tomada desde el padre para llegar al nodo
        self.path_cost = path_cost #costo desde el nodo raiz (estado inicial), hasta el nodo actual

    def __lt__(self, other): #comparar dos objetos de clase node basado en el costo
        return self.path_cost < other.path_cost

class Problem:
    def __init__(self, initial, goal, actions, result, action_cost, is_goal):
        self.initial = initial
        self.goal = goal
        self.actions = actions
        self.result = result
        self.action_cost = action_cost
        self.is_goal = is_goal

Actions = { #Definimos las accioes a las que puede ir un usuario desde una estación
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H', 'I'],
    'F': ['C', 'J'],
    'G': ['D'],
    'H': ['E'],
    'I': ['E', 'J'],
    'J': ['F', 'I']
}

Action_costs ={  #Se definen los costos (para todos igual a 1)
    ('A', 'B'): 1,
    ('A', 'C'): 1,
    ('B', 'A'): 1,
    ('B', 'D'): 1,
    ('B', 'E'): 1,
    ('C', 'A'): 1,
    ('C', 'F'): 1,
    ('D', 'B'): 1,
    ('D', 'G'): 1,
    ('E', 'B'): 1,
    ('E', 'H'): 1,
    ('E', 'I'): 1,
    ('F', 'C'): 1,
    ('F', 'J'): 1,
    ('G', 'D'): 1,
    ('H', 'E'): 1,
    ('I', 'E'): 1,
    ('I', 'J'): 1,
    ('J', 'F'): 1,
    ('J', 'I'): 1
}

def result(state, action):
    return action

def action_cost(state, action, result):
    return Action_costs.get((state, action), float('inf'))

def is_goal(state):
    return state == goal

def f(Nodo):
    return Nodo.path_cost

Initial = 'A'  # Estado inicial
goal = 'J' #Estado objetivo

def Expand(nodo, problem):
    s = nodo.state
    for action in problem.actions(s):
        ss= result(s, action) #Estado resultante de aplicar la acción
        cost= nodo.path_cost + problem.action_cost(s, action, ss)
        yield Node(ss, nodo, action, cost)

def best_first_search(problem, f):
     Nodo = Node(state=problem.initial)  # Crea el nodo raíz con el estado inicial del problema.
     frontera = [(f(Nodo), Nodo)]
     heapq.heapify(frontera)
     buscados= {Nodo.state: Nodo}

     while frontera:
         _,nodo = heapq.heappop(frontera) # Extrae el nodo con el valor mínimo de f de la frontera.
         if problem.is_goal(nodo.state):
             return nodo

         for hijo in Expand(nodo, problem):
             s = hijo.state
             if s not in buscados or hijo.path_cost < buscados[s].path_cost:
                    buscados[s] = hijo
                    heapq.heappush(frontera, (f(hijo), hijo))  # Añade el nodo hijo a la frontera

     return None  # No se encontró solución
tracemalloc.start()
t0 = perf_counter()

problem = Problem(Initial, goal, lambda s: Actions[s], result, action_cost, is_goal)
solucion = best_first_search(problem, f)

elapsed_ms = (perf_counter() - t0) * 1000
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

if solucion:
    path = []
    while solucion:
        path.append(solucion.state)
        solucion = solucion.parent
    path.reverse()
    print("Solution path:", path)
else:
    print("No solution found")

print(f"Tiempo gastado: {elapsed_ms:.3f}")
print(f"Memoria usada: {peak/1024:.1f}")


