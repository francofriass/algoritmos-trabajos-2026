#Ejercicio 5: Grafos
# Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios para resolver las tareas, listadas a continuación:
# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
# Red Hat, Debian, Arch;
# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
# Red Hat, Fedora hasta la impresora;
# d. encontrar el árbol de expansión mínima;
# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
# f. indicar desde que computadora del switch 01 es el camino más corto
# al servidor “MongoDB”;
# [230]
# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
# h. debe utilizar un grafo no dirigido.

from typing import Any, Optional
from list_ import List
from queue_ import Queue
from stacks import Stack
from heap import HeapMin



class Graph(List):


    class _nodeVertex():

        def __init__(self, value, other_values=None):
            self.value = value
            self.other_values = other_values
            self.edges = List()
            self.visited = False

            def _sort_by_destination(item):
                return item.destination

            self.edges.add_criterion('destination', _sort_by_destination)

        def __str__(self):
            return f"{self.value}"

    class _nodeEdge():

        def __init__(self, weight, destination):
            self.weight = weight
            self.destination = destination

        def __str__(self):
            return f"weight: {self.weight} -> destination: {self.destination}"

    def __init__(self, is_dir=True):
        self.is_dir = is_dir

        def sort_by_value(item):
            return item.value

        self.add_criterion('value', sort_by_value)


    def add_vertex(self, value: Any, other_values: Any = None) -> None:
        node_vertex = self._nodeVertex(value, other_values)
        self.append(node_vertex)

    def add_edge(self, weight: Any, origin: Any, destination: Any) -> None:

        pos_origin = self.search(origin, 'value')
        if pos_origin is None:
            print('no existe origien')
            return

        pos_destination = self.search(destination, 'value')
        if pos_destination is None:
            print('no existe el destino')
            return

        node_edge = self._nodeEdge(weight, destination)
        self[pos_origin].edges.append(node_edge)

        if origin != destination and not self.is_dir:
            node_edge = self._nodeEdge(weight, origin)
            self[pos_destination].edges.append(node_edge)

    def delete_vertex(self, value):
        result = self.delete_value(value, 'value')

        #limpiar aristas
        for vertex in self:
            # self.delete_edge(vertex.value, value)
            vertex.edges.delete_value(value, 'destination')

        return result

    def delete_edge(self, origin, destination) -> Optional[Any]:
        pos_origin = self.search(origin, 'value')
        if pos_origin is None:
            print('no existe origien')
            return

        result  = self[pos_origin].edges.delete_value(destination, 'destination')

        if not self.is_dir:
            pos_destination = self.search(destination, 'value')
            if pos_destination is not None:
                self[pos_destination].edges.delete_value(origin, 'destination')

        return result

    def show(self):
        for vertex in self:
            print(vertex)
            if len(vertex.edges) > 0:
                print('aristas ->')
                for edge in vertex.edges:
                    print(edge)

    def deep_show(self, origin) -> None:

        def _deep_show(origin) -> None:
            pos_origin = self.search(origin, 'value')
            if pos_origin is not None:
                visited = self[pos_origin].visited
                if not visited:
                    self[pos_origin].visited = True
                    print(self[pos_origin].value)
                    edges = self[pos_origin].edges
                    for edge in edges:
                        _deep_show(edge.destination)

        for vertex in self:
            vertex.visited = False

        _deep_show(origin)

    def amplitude_show(self, origin) -> None:
        for vertex in self:
            vertex.visited = False

        pending_queue = Queue()
        pos_origin = self.search(origin, 'value')
        if pos_origin is not None:
            visited = self[pos_origin].visited
            if not visited:
                pending_queue.arrive(self[pos_origin])
                while pending_queue.size() > 0:
                    # print()
                    # pending_queue.show()
                    # input()
                    # print()
                    vertex = pending_queue.attention()
                    if not vertex.visited:
                        vertex.visited = True
                        print(vertex.value)
                        edges = vertex.edges
                        for edge in edges:
                            # print(edge.destination)
                            pos_next_vertex = self.search(edge.destination, 'value')
                            pending_queue.arrive(self[pos_next_vertex])

    def dijkstra(self, origin):
        from math import inf

        no_visited = HeapMin()
        path = Stack()

        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            no_visited.arrive([vertex.value, vertex, None], distance)

        while no_visited.size() > 0:
            # for element in no_visited.elements:
            #     print(element)
            # print()
            # input()
            vertex = no_visited.attention()
            costo_nodo_actual = vertex[0]
            path.push([vertex[1][0], costo_nodo_actual, vertex[1][2]])
            edges = vertex[1][1].edges
            for edge in edges:
                pos = no_visited.search(edge.destination)
                if pos is not None:
                    if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                        no_visited.elements[pos][1][2] = vertex[1][0]
                        # el nuevo costo lo asigna change_priority (si se asigna antes,
                        # previous_priority queda igual a new_priority y el heap no se reordena)
                        no_visited.change_priority(pos, costo_nodo_actual + edge.weight)
        return path


    def kruskal(self, origin_vertex):
        def search_in_forest(forest, value):
            for index, tree in enumerate(forest):
                if value in tree:
                    return index

        forest = []
        edges = HeapMin()
        for vertex in self:
            forest.append(vertex.value)
            for edge in vertex.edges:
                edges.arrive([vertex.value, edge.destination], edge.weight)

        # print(forest)
        # for element in edges.elements:
        #     print(element )

        while len(forest) > 1 and edges.size() > 0:
            edge = edges.attention()
            origin = search_in_forest(forest, edge[1][0])
            destination = search_in_forest(forest, edge[1][1])
            if origin is not None and destination is not None:
                if origin != destination:
                    if origin > destination:
                        vertex_origin = forest.pop(origin)
                        vertex_destination = forest.pop(destination)
                    else:
                        vertex_destination = forest.pop(destination)
                        vertex_origin = forest.pop(origin)


                    if '-' not in vertex_origin and '-' not in vertex_destination:
                        forest.append(f'{vertex_origin}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_destination:
                        forest.append(vertex_origin+';'+f'{edge[1][0]}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_origin:
                        forest.append(vertex_destination+';'+f'{vertex_origin}-{edge[1][1]}-{edge[0]}')
                    else:
                        forest.append(vertex_origin+';'+vertex_destination+';'+f'{edge[1][0]}-{edge[1][1]}-{edge[0]}')

        from_vertex = search_in_forest(forest, origin_vertex)

        return forest[from_vertex] if from_vertex is not None else forest


    def exist_path(self, origin, destination):
        def __exist_path(graph, origin, destination):
            result = False
            vertex_pos = graph.search(origin, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    if graph[vertex_pos].value == destination:
                        return True
                    else:
                        for edge in graph[vertex_pos].edges:
                            destination_edge_pos = graph.search(edge.destination, 'value')
                            if not graph[destination_edge_pos].visited:
                                result = __exist_path(graph, graph[destination_edge_pos].value, destination)
                                if result:
                                    break
            return result

        for vertex in self:
            vertex.visited = False

        result = __exist_path(self, origin, destination)
        return result

# funciones para el ejercicio

def show_sweeps(graph):
    for notebook in ['Red Hat', 'Debian', 'Arch']:
        print(f'barrido en profundidad desde {notebook}:')
        graph.deep_show(notebook)
        print()
        print(f'barrido en amplitud desde {notebook}:')
        graph.amplitude_show(notebook)
        print()


def get_shortest_path(graph, origin, destination):
    camino_completo = []
    peso_total = None

    if graph.exist_path(origin, destination):
        paths = graph.dijkstra(origin)

        while paths.size() > 0:
            value = paths.pop()
            if value[0] == destination:
                if peso_total is None:
                    peso_total = value[1]
                camino_completo.append(value[0])
                destination = value[2]
        camino_completo.reverse()

    return camino_completo, peso_total

# ejercicio

#H
g = Graph(is_dir=False)


#A
g.add_vertex('Ubuntu', 'pc')
g.add_vertex('Mint', 'pc')
g.add_vertex('Manjaro', 'pc')
g.add_vertex('Parrot', 'pc')
g.add_vertex('Fedora', 'pc')

g.add_vertex('Debian', 'notebook')
g.add_vertex('Red Hat', 'notebook')
g.add_vertex('Arch', 'notebook')

g.add_vertex('Impresora', 'impresora')

g.add_vertex('Guaraní', 'servidor')
g.add_vertex('MongoDB', 'servidor')

g.add_vertex('Switch 1', 'switch')
g.add_vertex('Switch 2', 'switch')

g.add_vertex('Router 1', 'router')
g.add_vertex('Router 2', 'router')
g.add_vertex('Router 3', 'router')


# switch 1
g.add_edge(17, 'Switch 1', 'Debian')
g.add_edge(18, 'Switch 1', 'Ubuntu')
g.add_edge(22, 'Switch 1', 'Impresora')
g.add_edge(80, 'Switch 1', 'Mint')
g.add_edge(29, 'Switch 1', 'Router 1')

# routers
g.add_edge(37, 'Router 1', 'Router 2')
g.add_edge(43, 'Router 1', 'Router 3')
g.add_edge(50, 'Router 2', 'Router 3')

# router 2 y router 3
g.add_edge(25, 'Router 2', 'Red Hat')
g.add_edge(9, 'Router 2', 'Guaraní')
g.add_edge(61, 'Router 3', 'Switch 2')

# switch 2
g.add_edge(40, 'Switch 2', 'Manjaro')
g.add_edge(12, 'Switch 2', 'Parrot')
g.add_edge(5, 'Switch 2', 'MongoDB')
g.add_edge(56, 'Switch 2', 'Arch')
g.add_edge(3, 'Switch 2', 'Fedora')


print('a: nodos y su tipo')
for vertex in g:
    print(f'{vertex.value} -> {vertex.other_values}')


#B
print()
print('b: barridos desde las notebook')
show_sweeps(g)


#C
print('c: camino mas corto hasta la impresora')
for origin in ['Manjaro', 'Red Hat', 'Fedora']:
    camino_completo, peso_total = get_shortest_path(g, origin, 'Impresora')
    print(f'desde {origin}')
    print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')


#D
print()
print('d: arbol de expansion minima')
min_tree = g.kruskal('Router 1')

print(min_tree)
peso_total = 0
for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    print(f'origin {origin} destination {destination}')
    peso_total += int(weight)
print(f'peso total: {peso_total}')


#E
print()
print('e: pc con el camino mas corto hasta Guaraní')
pcs = []
for vertex in g:
    if vertex.other_values == 'pc':
        pcs.append(vertex.value)

mejor_pc = None
mejor_camino = []
menor_costo = None
for pc in pcs:
    camino_completo, peso_total = get_shortest_path(g, pc, 'Guaraní')
    print(f'desde {pc}: {"-".join(camino_completo)} con un costo de {peso_total}')
    if peso_total is not None and (menor_costo is None or peso_total < menor_costo):
        menor_costo = peso_total
        mejor_pc = pc
        mejor_camino = camino_completo
print(f'la pc con el camino mas corto es {mejor_pc}: {"-".join(mejor_camino)} con un costo de {menor_costo}')


#F
print()
print('f: computadora del Switch 1 con el camino mas corto hasta MongoDB')
computadoras = []
pos_switch = g.search('Switch 1', 'value')
for edge in g[pos_switch].edges:
    pos_neighbor = g.search(edge.destination, 'value')
    if g[pos_neighbor].other_values in ('pc', 'notebook'):
        computadoras.append(edge.destination)

mejor_computadora = None
mejor_camino = []
menor_costo = None
for computadora in computadoras:
    camino_completo, peso_total = get_shortest_path(g, computadora, 'MongoDB')
    print(f'desde {computadora}: {"-".join(camino_completo)} con un costo de {peso_total}')
    if peso_total is not None and (menor_costo is None or peso_total < menor_costo):
        menor_costo = peso_total
        mejor_computadora = computadora
        mejor_camino = camino_completo
print(f'la computadora con el camino mas corto es {mejor_computadora}: {"-".join(mejor_camino)} con un costo de {menor_costo}')


#G
print()
print('g: impresora conectada al Router 2')
g.delete_edge('Switch 1', 'Impresora')
g.add_edge(22, 'Router 2', 'Impresora')
print()
show_sweeps(g)