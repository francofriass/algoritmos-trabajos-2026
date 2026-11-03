# Ejercicio 1: 
# Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se conoce su 
# nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool) 
# para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:

# los índices de cada uno de los árboles deben ser nombre, número y tipo;
# mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
# mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
# realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
# mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
# mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
# determinar cuantos Pokémons tienen megaevolucion.
# determinar cuantos Pokémons tiene forma gigamax.
# cargue al menos 100 Pokémons.



# json y os esto carga los datos de los pokemones desde el archivo pokemons.json
import json
import os
from random import choice, shuffle

from tree import BinaryTree

with open(os.path.join(os.path.dirname(__file__), 'pokemons.json'), encoding='utf-8') as file:
    pokemons = json.load(file)


#funciones propias del ejercicio
def show_pokemon(pokemon: dict) -> None:
    print(f"numero: {pokemon['number']} - nombre: {pokemon['name']}")
    print(f"tipos: {', '.join(pokemon['types'])}")
    print(f"debil frente a: {', '.join(pokemon['weaknesses'])}")
    print(f"mega evolucion: {'si' if pokemon['mega'] else 'no'}")
    print(f"forma gigamax: {'si' if pokemon['gigamax'] else 'no'}")


def proximity_search_pokemon(tree: BinaryTree, prefix: str) -> None:

    def __proximity_search(root, prefix):
        if root is not None:
            __proximity_search(root.left, prefix)
            if prefix.lower() in root.value.lower():
                show_pokemon(root.other_values)
                print()
            __proximity_search(root.right, prefix)

    __proximity_search(tree.root, prefix)


def show_pokemons_by_type(tree: BinaryTree, pokemon_type: str) -> None:  #los tipos se repiten en el arbol, por eso recorro solo las ramas que pueden contenerlo

    def __show_by_type(root, pokemon_type):
        if root is not None:
            if pokemon_type <= root.value:
                __show_by_type(root.left, pokemon_type)
            if pokemon_type == root.value:
                print(root.other_values['name'])
            if pokemon_type >= root.value:
                __show_by_type(root.right, pokemon_type)

    __show_by_type(tree.root, pokemon_type)


def show_ascending_by_number(tree: BinaryTree) -> None:
    def __inorden(root):
        if root is not None:
            __inorden(root.left)
            print(f"{root.value} - {root.other_values['name']}")
            __inorden(root.right)

    __inorden(tree.root)


def show_ascending_by_name(tree: BinaryTree) -> None:
    def __inorden(root):
        if root is not None:
            __inorden(root.left)
            print(f"{root.other_values['number']} - {root.value}")
            __inorden(root.right)

    __inorden(tree.root)


def show_weak_against(tree: BinaryTree, target_types: list) -> None:
    def __inorden(root):
        if root is not None:
            __inorden(root.left)
            if any(pokemon_type in root.other_values['weaknesses'] for pokemon_type in target_types):
                print(root.value)
            __inorden(root.right)

    __inorden(tree.root)

def show_types_count(tree: BinaryTree) -> None:
    types_count = {}

    def __inorden(root):
        if root is not None:
            __inorden(root.left)
            types_count[root.value] = types_count.get(root.value, 0) + 1
            __inorden(root.right)

    __inorden(tree.root)

    for pokemon_type, count in types_count.items():
        print(f'{pokemon_type}: {count}')


def count_mega(tree: BinaryTree) -> int:

    def __count_mega(root):
        count = 0
        if root is not None:
            if root.left is not None:
                count += __count_mega(root.left)
            if root.other_values['mega']:
                count += 1
            if root.right is not None:
                count += __count_mega(root.right)
        return count

    return __count_mega(tree.root)


def count_gigamax(tree: BinaryTree) -> int:

    def __count_gigamax(root):
        count = 0
        if root is not None:
            if root.left is not None:
                count += __count_gigamax(root.left)
            if root.other_values['gigamax']:
                count += 1
            if root.right is not None:
                count += __count_gigamax(root.right)
        return count

    return __count_gigamax(tree.root)


# carga de los arboles
tree_name = BinaryTree()
tree_number = BinaryTree()
tree_type = BinaryTree()

shuffle(pokemons)

for pokemon in pokemons:
    tree_name.insert_node(pokemon['name'], pokemon)
    tree_number.insert_node(pokemon['number'], pokemon)
    for pokemon_type in pokemon['types']:
        tree_type.insert_node(pokemon_type, pokemon)

print()
print(f'ejercicio 1 del segundo parcial - {len(pokemons)} pokemons cargados')

#datos de un pokemon por numero
number = choice(pokemons)['number']
print(f'\n Pokemon numero {number} ')
node = tree_number.search(number)
if node is not None:
    show_pokemon(node.other_values)

#datos de pokemons por nombre (proximidad)
text = choice(['bul', 'char', 'eon', 'saur'])
print(f'\n Pokemones que comienzan o contienen "{text}" ')
proximity_search_pokemon(tree_name, text)

#nombres por tipo
for pokemon_type in ['fantasma', 'fuego', 'acero', 'eléctrico']:
    print(f' Pokemones de tipo {pokemon_type} ')
    show_pokemons_by_type(tree_type, pokemon_type)
    print()

#listados ascendentes por numero y por nombre
print(' Listado ascendente por numero ')
show_ascending_by_number(tree_number)

print('\n Listado ascendente por nombre  ')
show_ascending_by_name(tree_name)

#debiles frente a Jolteon, Lycanroc y Tyrantrum
for name in ['Jolteon', 'Lycanroc', 'Tyrantrum']:
    node = tree_name.search(name)
    if node is not None:
        types = node.other_values['types']
        print(f"\n Pokemones debiles frente a {name} (tipo {', '.join(types)}) ")
        show_weak_against(tree_name, types)

#cantidad de pokemons por tipo
print('\n Cantidad de pokemones por tipo ')
show_types_count(tree_type)

#megaevolucion y gigamax
print(f'\nPokemons con megaevolucion: {count_mega(tree_number)}')
print(f'Pokemones con forma gigamax: {count_gigamax(tree_number)}')

#listado por nivel por nombre
print('\n Listado por nivel por nombre ')
tree_name.by_level()