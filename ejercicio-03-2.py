from collections import deque
import time
import tracemalloc

class Node:
    def __init__(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth

def expand(graph, node):
    children = []
    for a in actions(graph, node.state):
        s2 = result(node.state, a)
        children.append(Node(s2, parent=node, depth=node.depth + 1))
    return children

def is_cycle(node):
    cur = node.parent
    while cur is not None:
        if cur.state == node.state:
            return True
        cur = cur.parent
    return False

def actions(graph, state):
    return graph.get(state, [])

def result(state, action):
    return action

def is_goal(state, goal):
    return state == goal

def expand(graph, node):
    children = []
    for a in actions(graph, node.state):
        s2 = result(node.state, a)
        children.append(Node(s2, parent=node, depth=node.depth + 1))
    return children

def is_cycle(node):
    cur = node.parent
    while cur is not None:
        if cur.state == node.state:
            return True
        cur = cur.parent
    return False

def depth_limited_search(graph, initial, goal, limit):
    frontier = deque([Node(initial)])
    cutoff = False
    while frontier:
        node = frontier.pop()
        if is_goal(node.state, goal):
            return node
        if node.depth == limit:
            cutoff = True
        else:
            for child in expand(graph, node):
                if not is_cycle(child):
                    frontier.append(child)
    return 'cutoff' if cutoff else 'failure'

def iterative_deepening_search(graph, initial, goal, max_depth=50):
    for d in range(max_depth + 1):
        r = depth_limited_search(graph, initial, goal, d)
        if r != 'cutoff':
            return r
    return None

def reconstruct_path(node):
    path = []
    while isinstance(node, Node) and node is not None:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H', 'I'],
    'F': ['C', 'J'],
    'G': ['D'],
    'H': ['E'],
    'I': ['E', 'J'],
    'J': ['F', 'I'],
}

START = 'A'
GOAL = 'J'

tracemalloc.start()
t0 = time.perf_counter()
sol = iterative_deepening_search(graph, START, GOAL, max_depth=50)
t1 = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

if isinstance(sol, Node):
    path = reconstruct_path(sol)
    print("Algorithm: IDS")
    print("Start:", START, "Goal:", GOAL)
    print("Solution path:", path)
    print("Steps:", len(path) - 1)
    print("Execution time (s):", round(t1 - t0, 6))
    print("Peak memory (KiB):", round(peak / 1024, 3))
else:
    print("Algorithm: IDS")
    print("Start:", START, "Goal:", GOAL)
    print("Result:", sol)
    print("Execution time (s):", round(t1 - t0, 6))
    print("Peak memory (KiB):", round(peak / 1024, 3))