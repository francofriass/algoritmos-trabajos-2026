# Ejercicio 2: 
# Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:

# cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
# hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
# determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
# cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
# calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
# indicar qué personajes aparecieron en los nueve episodios de la saga.

from graph import Graph


#episodios (1 a 9) en los que aparece cada personaje
#los nombres los puse sin guion porque el kruskal de graph.py usa '-' como separador
characters = {
    'Luke Skywalker': {3, 4, 5, 6, 7, 8, 9},
    'Darth Vader': {3, 4, 5, 6},
    'Yoda': {1, 2, 3, 5, 6, 8},
    'Boba Fett': {2, 5, 6},
    'C3PO': {1, 2, 3, 4, 5, 6, 7, 8, 9},
    'Leia': {3, 4, 5, 6, 7, 8, 9},
    'Rey': {7, 8, 9},
    'Kylo Ren': {7, 8, 9},
    'Chewbacca': {3, 4, 5, 6, 7, 8, 9},
    'Han Solo': {4, 5, 6, 7, 9},
    'R2D2': {1, 2, 3, 4, 5, 6, 7, 8, 9},
    'BB8': {7, 8, 9},
}

total_episodes = 9


#funciones propias del ejercicio
def show_min_tree(graph: Graph, origin: str) -> None:
    min_tree = graph.kruskal(origin)

    peso_total = 0
    for edge in min_tree.split(';'):
        edge_origin, edge_destination, weight = edge.split('-')
        print(f'{edge_origin} - {edge_destination} (episodios: {weight})')
        peso_total += int(weight)
    print(f'peso total: {peso_total}')


def max_shared_episodes(graph: Graph) -> tuple:  #cada arista esta en los dos vertices, se toma solo una vez por par

    maximum = 0
    pairs = []

    for vertex in graph:
        for edge in vertex.edges:
            if vertex.value < edge.destination:
                if edge.weight > maximum:
                    maximum = edge.weight
                    pairs = [(vertex.value, edge.destination)]
                elif edge.weight == maximum:
                    pairs.append((vertex.value, edge.destination))

    return maximum, pairs


def characters_in_all_episodes(graph: Graph) -> list:    #si dos personajes comparten los nueve episodios ambos aparecieron en los nueve

    result = []

    for vertex in graph:
        for edge in vertex.edges:
            if edge.weight == total_episodes and vertex.value not in result:
                result.append(vertex.value)

    return result


def shortest_path(graph: Graph, origin: str, destination: str) -> None:
    if graph.exist_path(origin, destination):
        paths = graph.dijkstra(origin)

        peso_total = None
        camino_completo = []
        value_destination = destination

        while paths.size() > 0:
            value = paths.pop()
            if value[0] == value_destination:
                if peso_total is None:
                    peso_total = value[1]
                camino_completo.append(value[0])
                value_destination = value[2]
        camino_completo.reverse()
        print(f'el camino mas corto de {origin} a {destination} es: {" -> ".join(camino_completo)} con un costo de {peso_total}')
    else:
        print(f'no existe camino de {origin} a {destination}')


#carga del grafo: cada arista pesa la cantidad de episodios que comparten
star_wars = Graph(is_dir=False)

for character in characters:
    star_wars.add_vertex(character)

names = list(characters)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        shared = characters[names[i]] & characters[names[j]]
        if len(shared) > 0:
            star_wars.add_edge(len(shared), names[i], names[j])

print()
print(f'ejercicio 2 del segundo parcial - {len(star_wars)} personajes cargados')

#arbol de expansion minimo
for character in ['C3PO', 'Yoda', 'Leia']:
    print(f'\n Arbol de expansion minimo desde {character} ')
    show_min_tree(star_wars, character)
    
#el grafo es conexo, kruskal devuelve el mismo arbol (peso total 21) 
#sin importar el vertice de origen

#maximo de episodios compartidos
maximum, pairs = max_shared_episodes(star_wars)
print(f'\n Maximo de episodios compartidos: {maximum} ')
for character_a, character_b in pairs:
    print(f'{character_a} y {character_b}')

#caminos mas cortos
print('\n Caminos mas cortos ')
shortest_path(star_wars, 'C3PO', 'R2D2')
shortest_path(star_wars, 'Yoda', 'Darth Vader')

#personajes en los nueve episodios
print(f'\n Personajes que aparecieron en los {total_episodes} episodios ')
for character in characters_in_all_episodes(star_wars):
    print(character)