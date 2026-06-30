import random
from super_heroes_data import superheroes

def buscar_capitan_america(lista_heroes: list) -> bool:
    if not lista_heroes:
        return False
    if lista_heroes[0] == "Captain America":
        return True
    return buscar_capitan_america(lista_heroes[1:])


def listar_superheroes(lista_heroes: list) -> None:
    if not lista_heroes:
        return      
    print(f"{lista_heroes[0]}")
    listar_superheroes(lista_heroes[1:])

if __name__ == "__main__": 
    todos_los_nombres = [heroe["name"] for heroe in superheroes]
    lista_15_azar = random.sample(todos_los_nombres, 15)
    
    print("-" * 40)
    print("Listado de los 15 super héroes: ")
    print("-" * 40)
    listar_superheroes(lista_15_azar)
    print(" Buscar al capitan América: ")
    encontrado = buscar_capitan_america(lista_15_azar)
    
    if encontrado:
        print("El Capitán América si está en la lista")
    else:
        print("El Capitán América no está en la lista")