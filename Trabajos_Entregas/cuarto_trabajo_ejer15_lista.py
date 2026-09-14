from list_ import List

datos_entrenadores = [
    {"nombre": "Ash", "torneos": 5, "ganadas": 50, "perdidas": 10, "pokemons": [
        {"nombre": "Pikachu", "nivel": 50, "tipo": "Eléctrico", "subtipo": None},
        {"nombre": "Charizard", "nivel": 60, "tipo": "Fuego", "subtipo": "Volador"},
        {"nombre": "Bulbasaur", "nivel": 40, "tipo": "Planta", "subtipo": "Veneno"}
    ]},
    {"nombre": "Misty", "torneos": 2, "ganadas": 30, "perdidas": 5, "pokemons": [
        {"nombre": "Starmie", "nivel": 45, "tipo": "Agua", "subtipo": "Psíquico"},
        {"nombre": "Wingull", "nivel": 20, "tipo": "Agua", "subtipo": "Volador"} # Agua/Volador
    ]},
    {"nombre": "Goh", "torneos": 0, "ganadas": 20, "perdidas": 20, "pokemons": [
        {"nombre": "Cinderace", "nivel": 45, "tipo": "Fuego", "subtipo": None},
        {"nombre": "Pikachu", "nivel": 10, "tipo": "Eléctrico", "subtipo": None},
        {"nombre": "Pikachu", "nivel": 12, "tipo": "Eléctrico", "subtipo": None} # Pokémon repetido
    ]},
    {"nombre": "Leon", "torneos": 10, "ganadas": 100, "perdidas": 2, "pokemons": [
        {"nombre": "Charizard", "nivel": 90, "tipo": "Fuego", "subtipo": "Volador"},
        {"nombre": "Tyrantrum", "nivel": 85, "tipo": "Roca", "subtipo": "Dragón"},
        {"nombre": "Terrakion", "nivel": 80, "tipo": "Roca", "subtipo": "Lucha"}
    ]}
]

class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        sub = f"/{self.subtipo}" if self.subtipo else ""
        return f"{self.nombre} (Nvl: {self.nivel}) - {self.tipo}{sub}"

class Entrenador:
    def __init__(self, nombre, torneos, ganadas, perdidas):
        self.nombre = nombre
        self.torneos = torneos
        self.ganadas = ganadas
        self.perdidas = perdidas
        self.pokemons = List()
        self.pokemons.add_criterion('nombre', by_name)
        self.pokemons.add_criterion('nivel', by_level)

    def __str__(self):
        return f"Entrenador: {self.nombre} | Torneos: {self.torneos} | Victorias: {self.ganadas} | Derrotas: {self.perdidas}"

def by_name(item):
    return item.nombre

def by_level(item):
    return item.nivel

def by_tournaments(item):
    return item.torneos

#a
def cantidad_pokemons_entrenador(lista, nombre_entrenador):
    idx = lista.search(nombre_entrenador, 'nombre')
    if idx is not None:
        entrenador = lista[idx]
        print(f"{entrenador.nombre} tiene {entrenador.pokemons.size()} Pokémons.")

#b
def entrenadores_mas_de_tres_torneos(lista):
    print("Entrenadores con más de 3 torneos ganados:")
    for entrenador in lista:
        if entrenador.torneos > 3:
            print(f"- {entrenador.nombre} ({entrenador.torneos} torneos)")

#c
def pokemon_mayor_nivel_mejor_entrenador(lista):
    if lista.size() == 0: return
    mejor_entrenador = max(lista, key=lambda e: e.torneos)
    
    if mejor_entrenador.pokemons.size() > 0:
        poke_mayor = max(mejor_entrenador.pokemons, key=lambda p: p.nivel)
        print(f"El mejor entrenador es {mejor_entrenador.nombre} y su Pokémon de mayor nivel es: {poke_mayor}")

#d
def mostrar_datos_completos(lista, nombre_entrenador):
    idx = lista.search(nombre_entrenador, 'nombre')
    if idx is not None:
        e = lista[idx]
        print(e)
        print("Sus Pokémons:")
        e.pokemons.show()
        
#e
def entrenadores_alto_porcentaje_victorias(lista):
    print("Entrenadores con más del 79 porciento de victorias:")
    for e in lista:
        total_batallas = e.ganadas + e.perdidas
        if total_batallas > 0:
            porcentaje = (e.ganadas / total_batallas) * 100
            if porcentaje > 79:
                print(f"- {e.nombre} ({porcentaje:.1f}%)")

#f
def entrenadores_tipos_especificos(lista):
    print("Entrenadores con (Fuego Y Planta) O (Agua y Volador):")
    for e in lista:
        tiene_fuego = False
        tiene_planta = False
        tiene_agua_volador = False
        
        for p in e.pokemons:
            tipo = p.tipo.lower()
            sub = p.subtipo.lower() if p.subtipo else ""
            
            if tipo == 'fuego': tiene_fuego = True
            if tipo == 'planta': tiene_planta = True
            if tipo == 'agua' and sub == 'volador': tiene_agua_volador = True
            
        if (tiene_fuego and tiene_planta) or tiene_agua_volador:
            print(f"- {e.nombre}")

#g
def promedio_nivel_pokemons(lista, nombre_entrenador):
    idx = lista.search(nombre_entrenador, 'nombre')
    if idx is not None:
        e = lista[idx]
        if e.pokemons.size() > 0:
            suma_niveles = sum(p.nivel for p in e.pokemons)
            promedio = suma_niveles / e.pokemons.size()
            print(f"El promedio de nivel de los Pokémons de {e.nombre} es: {promedio:.1f}")

#h
def cuantos_tienen_pokemon(lista, nombre_pokemon):
    contador = 0
    for e in lista:
        if e.pokemons.search(nombre_pokemon, 'nombre') is not None:
            contador += 1
    print(f"Cantidad de entrenadores que tienen a {nombre_pokemon}: {contador}")

#i
def entrenadores_con_repetidos(lista):
    print("Entrenadores con Pokémons repetidos:")
    for e in lista:
        nombres = [p.nombre for p in e.pokemons]
        if len(set(nombres)) < len(nombres):
            print(f"- {e.nombre}")

#j
def entrenadores_con_pokemons_buscados(lista, buscados):
    print(f"Entrenadores que tienen al menos uno de estos: {', '.join(buscados)}")
    for e in lista:
        tiene = False
        for poke_buscado in buscados:
            if e.pokemons.search(poke_buscado, 'nombre') is not None:
                tiene = True
                break
        if tiene:
            print(f"- {e.nombre}")

#k
def validar_pokemon_entrenador(lista, nombre_entrenador, nombre_pokemon):
    idx_e = lista.search(nombre_entrenador, 'nombre')
    if idx_e is not None:
        e = lista[idx_e]
        idx_p = e.pokemons.search(nombre_pokemon, 'nombre')
        if idx_p is not None:
            p = e.pokemons[idx_p]
            print(f"Confirmado {e.nombre} tiene a {p.nombre}.")
            print(f"Datos Entrenador: {e}")
            print(f"Datos Pokémon: {p}")
        else:
            print(f"{e.nombre} NO tiene a {nombre_pokemon}.")
    else:
        print(f"No se encontró al entrenador {nombre_entrenador}.")


if __name__ == '__main__':
    
    lista_entrenadores = List()
    lista_entrenadores.add_criterion('nombre', by_name)
    lista_entrenadores.add_criterion('torneos', by_tournaments)

    for data_e in datos_entrenadores:
        entrenador = Entrenador(data_e['nombre'], data_e['torneos'], data_e['ganadas'], data_e['perdidas'])
        for data_p in data_e['pokemons']:
            pokemon = Pokemon(data_p['nombre'], data_p['nivel'], data_p['tipo'], data_p['subtipo'])
            entrenador.pokemons.append(pokemon)
        lista_entrenadores.append(entrenador)


    cantidad_pokemons_entrenador(lista_entrenadores, "Ash")

    entrenadores_mas_de_tres_torneos(lista_entrenadores)

    pokemon_mayor_nivel_mejor_entrenador(lista_entrenadores)

    mostrar_datos_completos(lista_entrenadores, "Misty")

    entrenadores_alto_porcentaje_victorias(lista_entrenadores)

    entrenadores_tipos_especificos(lista_entrenadores)

    promedio_nivel_pokemons(lista_entrenadores, "Ash")

    cuantos_tienen_pokemon(lista_entrenadores, "Charizard")

    entrenadores_con_repetidos(lista_entrenadores)

    entrenadores_con_pokemons_buscados(lista_entrenadores, ["Tyrantrum", "Terrakion", "Wingull"])

    validar_pokemon_entrenador(lista_entrenadores, "Leon", "Tyrantrum")