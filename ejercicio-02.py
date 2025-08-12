import heapq #El módulo heapq implementa colas de prioridad (heaps)
     

class Node:
    """
    A node in the search tree. Contains the position, a reference to its parent node,
    the cost of the path from the start to this node, and the action that led to it.
    """
    def __init__(self, position, parent=None, path_cost=0, action=None): # ADDED 'action'
        self.position = position
        self.parent = parent
        self.path_cost = path_cost  # This is g(n), the cost from the start
        self.action = action        # The action taken to get to this node

    def __lt__(self, other):
        """
        Comparison method for the priority queue to handle nodes with equal priority.
        """
        return self.path_cost < other.path_cost

class Problem:
    """
    Defines the problem structure, including actions, initial state, and goal state.
    """
    def __init__(self, initial_state=None, goal_state=None):
        self.actions = {
            (0, 1): "Right",
            (0, -1): "Left",
            (1, 0): "Down",
            (-1, 0): "Up"
        }
        self.initial_state = initial_state
        self.goal_state = goal_state

    def get_actions(self):
        return self.actions.items()

def find_exit(maze):
    start = None  # Posición inicial basado en la documentación suministrada
    end = None    # Posición de la salida basado en la documentación suministrada

    for r, row in enumerate(maze):
        for c, val in enumerate(row):
            if val == 'S':
                start = (r, c)
            elif val == 'E':
                goal = (r, c)
    
    if start is None or goal is None:
        return "Start or Goal not found in the maze."

    #DEFINA el conjunto de actions posibles#

    problem=Problem(initial_state=start, goal_state=goal)#COMPLETE LA DEFINICIÓN DEL OBJETO Y ADAPTELO EN LOS PUNTOS QUE LO REQUIERAN

    def manhatan_distance(pos, goal_pos):
        return abs(pos[0] - goal_pos[0]) + abs(pos[1] - goal_pos[1])  # Distancia de Manhattan

    def get_neighbors(pos):  #ESTA ES LA FUNCIÓN QUE DEBERIA AJUSTAR PARA HACER TRACKING DE LOS MOVIMIENTOS (Up, Down, Right, Left)
        neighbors = [] #lista de vecinos
        for move_vector, action_name in problem.get_actions():  #Tenga en cuenta que para que esto sea funcional ya debio haber definido el objeto problem
            neighbor_pos = (pos[0] + move_vector[0], pos[1] + move_vector[1])
            if not (0 <= neighbor_pos[0] < len(maze) and 0 <= neighbor_pos[1] < len(maze[0])):
                continue
            if maze[neighbor_pos[0]][neighbor_pos[1]] != "#": #si el vecino es diferente a "#" pared agregarlo a la lista de vecinos                neighbors.append(neighbor)
              neighbors.append((action_name, neighbor_pos))  # Agrega la acción junto con la posición del vecino
        return neighbors

    start_node = Node(problem.initial_state, path_cost=0)
    priority = start_node.path_cost + manhatan_distance(start_node.position, problem.goal_state)
    frontier = [(priority, start_node)]
    heapq.heapify(frontier)
    reached = {problem.initial_state: start_node}

    while frontier:
        _, current_node = heapq.heappop(frontier)
        if current_node.position == problem.goal_state:
            return reconstruct_path(current_node)

        for action, neighbor_pos in get_neighbors(current_node.position):
            new_cost = current_node.path_cost + 1 
            if neighbor_pos not in reached or new_cost < reached[neighbor_pos].path_cost:
                new_node = Node(neighbor_pos, parent=current_node, path_cost=new_cost, action=action)  # Incluye la acción
                reached[neighbor_pos] = new_node
                priority = new_cost + manhatan_distance(neighbor_pos, problem.goal_state)
                heapq.heappush(frontier, (priority, new_node))

    return None  # No se encontró salida
     

def reconstruct_path(node):  #AJUSTAR FUNCIONES PARA ADEMAS DE LAS POSICIONES, MOSTRAR LAS ACCIONES TOMADAS
    path = []
    while node.parent is not None:
        path.append((node.action, node.position))  # Agrega la acción junto con la posición
        node = node.parent
    path.append(("Start", node.position))  # Agrega la posición inicial
    path.reverse()
    return path

     

maze = [
    ["#", "#", "#", "#", "#", "#", "#","#"],
    ["#", "S", "#", " ", "#", " ", "E","#"],
    ["#", " ", " ", " ", "#", " ", " ","#"],
    ["#", " ", "#", " ", " ", " ", "#","#"],
    ["#", "#", "#", "#", "#", "#", "#","#"],
    ["#", "#", "#", "#", "#", "#", "#","#"]
]
path = find_exit(maze)

if path:
    print("Path to exit found! 🗺️\n")
    for step in path:
        action, position = step
        print(f"-> Action: {action}, Position: {position}")
else:
    print("No path to exit was found.")

print("Path to exit:", path)