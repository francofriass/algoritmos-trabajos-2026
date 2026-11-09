#  . Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;# II. realizar un barrido ordenado alfabéticamente de cada árbol.

from super_heroes_data import superheroes
from tree import BinaryTree

arbol_marvel = BinaryTree()

print(f'cantidad de elementos {len(superheroes)}')

# A
for marvel_character in superheroes:
    arbol_marvel.insert_node(marvel_character['name'], other_value=marvel_character)

# B
print("\n--- B")
arbol_marvel.inorden_villain()

# C
print("\n--- C")
arbol_marvel.inorden_hero_star_with('C')

# D
print("\n--- D")
print(f'cantidad de heroes: {arbol_marvel.count_heroes()}')

# E
print("\n--- E")
search_str = input('ingrese lo que quiere buscar: ')
arbol_marvel.proxy_search(search_str.lower())

search_str = input('ingrese lo que quiere modificar: ')

node = arbol_marvel.search(search_str)
if node is not None:
    new_name = input('ingrese el nuevo nombre: ')
    delete_value, delete_other_value = arbol_marvel.delete_node(node.value)
    delete_other_value['name'] = new_name
    arbol_marvel.insert_node(new_name, delete_other_value)
    nodo_modificado = arbol_marvel.search(new_name)
    if nodo_modificado is not None:
        print(f"El personaje fue encontrado en el árbol con el nombre: {nodo_modificado.value}")
else:
    print("No se encontró el personaje especificado.")

# F
print("\n--- F.")
arbol_marvel.postorden_hero()

# G
print("\n--- G")
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

nodos_heroes = 0
nodos_villanos = 0

for marvel_character in superheroes:
    if marvel_character.get('is_villain', False):
        arbol_villanos.insert_node(marvel_character['name'], marvel_character)
        nodos_villanos += 1
    else:
        arbol_heroes.insert_node(marvel_character['name'], marvel_character)
        nodos_heroes += 1

print(f"Cantidad de nodos en el árbol de Héroes: {nodos_heroes}")
print(f"Cantidad de nodos en el árbol de Villanos: {nodos_villanos}")

print("\n Barrido alfabético del árbol de Héroes:")
arbol_heroes.inorden()

print("\n Barrido alfabético del árbol de Villanos:")
arbol_villanos.inorden()
