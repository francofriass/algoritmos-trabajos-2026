from list_ import List
from cola import Queue
from super_heroes_data import superheroes

#--------------------------------------------
def by_name(item):
    return item['name']

def by_real_name(item):
    return str(item['real_name'])

def by_first_appearance(item):
    return item['first_appearance']

#--------------------------------------------
def obtener_villanos(lista_p: List) -> List:
    aux = List()
    for heroe in lista_p:
        if heroe['is_villain']:
            aux.append(heroe)
    return aux

def listar_villanos_viejos(lista_villanos: List):
    cola_v = Queue()
    
    for villano in lista_villanos:
        cola_v.arrive(villano)
        
    while cola_v.size() > 0:
        v = cola_v.attention()
        if v['first_appearance'] < 1980:
            print(f"{v['name']} ({v['first_appearance']})")

def listar_por_iniciales(lista_p: List, iniciales: tuple):
    for heroe in lista_p:
        if not heroe['is_villain'] and heroe['name'].startswith(iniciales):
            print(heroe['name'])

def buscar_en_bio(lista_p: List, palabras: tuple):
    for heroe in lista_p:
        bio = heroe['short_bio'].lower()
        for palabra in palabras: #use una busqueda simple porque ya conozco el dataset provisto y se de antemano que no va a dar un falso positivo
            if palabra in bio:
                print(f"{heroe['name']}: (palabra clave: {palabra})")
                break  #corto la busqueda 

#--------------------------------------------
def ejercicio_2():
    lista_marvel = List()
    lista_marvel.add_criterion('name', by_name)
    lista_marvel.add_criterion('real_name', by_real_name)
    lista_marvel.add_criterion('first_appearance', by_first_appearance)
    
    for heroe in superheroes:
        lista_marvel.append(heroe)

    #[A]
    print("\n Punto A: Ordenado por nombre: ")
    lista_marvel.sort_by_criterion('name')
    for heroe in lista_marvel[:15]: #pongo los primeros 15 porque sino se hace muy larga la salida y no es necesario mostrar todos los personajes
        print(heroe['name'])
    print("(primeros 15 personajes ordenados por nombre)")

    #[B]
    print("\n Punto B: Posiciones: ")
    print(f"Posicion The Thing: {lista_marvel.search('The Thing', 'name')}")
    print(f"Posicion Rocket Raccoon: {lista_marvel.search('Rocket Raccoon', 'name')}")

    #[C]
    print("\n Punto C: Villanos: ")
    lista_de_villanos = obtener_villanos(lista_marvel)
    for v in lista_de_villanos[:15]:
        print(v['name'])
    print("(primeros 15 villanos)")    

    #[D]
    print("\n Punto D: Villanos antes de 1980")
    listar_villanos_viejos(lista_de_villanos)

    #[E]
    print("\n Punto E: Iniciales Bl, G, My, W")
    listar_por_iniciales(lista_marvel, ('Bl', 'G', 'My', 'W'))

    #[F]
    print("\n Punto F: Ordenado por nombre real: ")
    lista_marvel.sort_by_criterion('real_name')
    for heroe in lista_marvel[:15]: 
        print(f"{heroe['real_name']} (Heroe: {heroe['name']})")
    print("(primeros 15 nombres)")
    
    #[G]
    print("\n Punto G: Ordenado por fecha de aparicion: ")
    lista_marvel.sort_by_criterion('first_appearance')
    cont = 0
    for heroe in lista_marvel:
        if not heroe['is_villain']:
            print(f"{heroe['name']} ({heroe['first_appearance']})")
            cont += 1
            if cont == 15: 
                break
    print("(primeros 15)")        

    #[H]
    print("\n Punto H: Modificar Ant Man: ")
    posicion_antman = lista_marvel.search('Ant Man', 'name')
    if posicion_antman is not None:
        lista_marvel[posicion_antman]['real_name'] = 'Scott Lang'
        print("Nombre modificado con exito.")
        print(f"Datos actualizados = Heroe: {lista_marvel[posicion_antman]['name']}, Nuevo Nombre Real: {lista_marvel[posicion_antman]['real_name']}")

    #[I]
    print("\n Punto I: Bio con palabras clave: ")
    buscar_en_bio(lista_marvel, ('time-traveling', 'suit'))

    #[J]
    print("\n Punto J: Eliminar personajes: ")
    electro_eliminado = lista_marvel.delete_value('Electro', 'name')
    zemo_eliminado = lista_marvel.delete_value('Baron Zemo', 'name')
    
    if electro_eliminado: 
        print(f"Personaje eliminado: {electro_eliminado['name']}")
        print(f"Info: Nombre Real: {electro_eliminado['real_name']}, Aparicion: {electro_eliminado['first_appearance']}")
        print(f"Bio: {electro_eliminado['short_bio']}\n")
    else:
        print("Electro no se elimino porque no estaba en la lista.\n")
        
    if zemo_eliminado: 
        print(f"Personaje eliminado: {zemo_eliminado['name']}")
        print(f"Info: Nombre Real: {zemo_eliminado['real_name']}, Aparicion: {zemo_eliminado['first_appearance']}")
        print(f"Bio: {zemo_eliminado['short_bio']}")
    else:
        print("Baron Zemo no se elimino porque no estaba en la lista.")

if __name__ == "__main__":
    ejercicio_2()