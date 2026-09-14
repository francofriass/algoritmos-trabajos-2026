from list_ import List

superheroes = [
    {"nombre": "Spider-Man", "anio_aparicion": 1962, "casa": "Marvel", "biografia": "Peter Parker fue mordido por una araña radiactiva..."},
    {"nombre": "Iron Man", "anio_aparicion": 1963, "casa": "Marvel", "biografia": "Tony Stark construyó una armadura tecnológica para escapar..."},
    {"nombre": "Wolverine", "anio_aparicion": 1974, "casa": "Marvel", "biografia": "Logan posee un esqueleto recubierto de adamantium..."},
    {"nombre": "Thor", "anio_aparicion": 1962, "casa": "Marvel", "biografia": "Dios nórdico del trueno e hijo de Odín..."},
    {"nombre": "Black Widow", "anio_aparicion": 1964, "casa": "Marvel", "biografia": "Natasha Romanoff fue entrenada desde niña..."},
    {"nombre": "Batman", "anio_aparicion": 1939, "casa": "DC", "biografia": "Bruce Wayne usa su inteligencia, fortuna y un traje con muchas herramientas..."},
    {"nombre": "Superman", "anio_aparicion": 1938, "casa": "DC", "biografia": "Kal-El fue enviado desde el planeta Krypton..."},
    {"nombre": "Mujer Maravilla", "anio_aparicion": 1941, "casa": "DC", "biografia": "Diana, princesa de las Amazonas..."},
    {"nombre": "Flash", "anio_aparicion": 1956, "casa": "DC", "biografia": "Barry Allen era un científico forense..."},
    {"nombre": "Linterna Verde", "anio_aparicion": 1959, "casa": "DC", "biografia": "Hal Jordan fue elegido por el anillo de poder..."},
    {"nombre": "Dr. Strange", "anio_aparicion": 1963, "casa": "Desconocida", "biografia": "Stephen Strange es el Hechicero Supremo..."},
    {"nombre": "Capitana Marvel", "anio_aparicion": 1968, "casa": "Marvel", "biografia": "Carol Danvers, ex piloto de la Fuerza Aérea..."},
    {"nombre": "Star-Lord", "anio_aparicion": 1976, "casa": "Marvel", "biografia": "Peter Quill, líder de los Guardianes de la Galaxia..."}
]

class Superhero():
    def __init__(self, nombre, anio, casa, bio):
        self.name = nombre
        self.year = anio
        self.house = casa
        self.bio = bio

    def __str__(self):
        return f"{self.name} - {self.year} - {self.house}"

def by_name(item):
    return item.name

def by_year(item):
    return item.year

#a
def eliminar_linterna_verde(lista):
    eliminado = lista.delete_value("Linterna Verde", 'name')
    if eliminado:
        print(f"Se eliminó correctamente a: {eliminado.name}")
    else:
        print("No se encontró a Linterna Verde en la lista.")

#b
def mostrar_anio_wolverine(lista):
    idx = lista.search("Wolverine", 'name')
    if idx is not None:
        print(f"El año de aparición de Wolverine es: {lista[idx].year}")

#c
def cambiar_casa_dr_strange(lista):
    idx = lista.search("Dr. Strange", 'name')
    if idx is not None:
        lista[idx].house = 'Marvel'
        print("Se actualizó la casa de Dr. Strange a Marvel.")

#d
def mostrar_traje_armadura(lista):
    print("Superhéroes que mencionan 'traje' o 'armadura':")
    for hero in lista:
        bio_minuscula = hero.bio.lower()
        if 'traje' in bio_minuscula or 'armadura' in bio_minuscula:
            print(f"- {hero.name}")

#e
def mostrar_anteriores_1963(lista):
    print("Superhéroes con fecha de aparición anterior a 1963:")
    for hero in lista:
        if hero.year < 1963:
            print(f"- {hero.name} ({hero.house})")

#f
def mostrar_casa_capitana_y_mujer_maravilla(lista):
    for personaje in ["Capitana Marvel", "Mujer Maravilla"]:
        idx = lista.search(personaje, 'name')
        if idx is not None:
            print(f"{personaje} pertenece a la casa: {lista[idx].house}")

#g
def mostrar_info_flash_starlord(lista):
    for personaje in ["Flash", "Star-Lord"]:
        idx = lista.search(personaje, 'name')
        if idx is not None:
            h = lista[idx]
            print(f"[{h.name}] | Año: {h.year} | Casa: {h.house} | Bio: {h.bio}")

#h
def listar_comienzan_b_m_s(lista):
    print("Superhéroes que comienzan con B, M y S:")
    lista.filter_start_with(('B', 'M', 'S'))

#i, j
def contar_por_casa(lista):
    contadores = {}
    for hero in lista:
        contadores[hero.house] = contadores.get(hero.house, 0) + 1
    
    for casa, cantidad in contadores.items():
        print(f"Casa {casa}: {cantidad} superhéroes")


if __name__ == '__main__':
    
    list_heroes = List()
    list_heroes.add_criterion('name', by_name)
    list_heroes.add_criterion('year', by_year)

    for hero in superheroes:
        list_heroes.append(
            Superhero(hero['nombre'], hero['anio_aparicion'], hero['casa'], hero['biografia'])
        )


    eliminar_linterna_verde(list_heroes)

    mostrar_anio_wolverine(list_heroes)

    cambiar_casa_dr_strange(list_heroes)

    mostrar_traje_armadura(list_heroes)

    mostrar_anteriores_1963(list_heroes)

    mostrar_casa_capitana_y_mujer_maravilla(list_heroes)

    mostrar_info_flash_starlord(list_heroes)

    listar_comienzan_b_m_s(list_heroes)

    contar_por_casa(list_heroes)