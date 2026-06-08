import random
from cola import Queue

def reporte_shield_mcu(cola: Queue):
    cantidad_elementos = cola.size()
    
    nombre_capitana_marvel = "No encontrada en el escaneo"
    heroe_scott_lang = "No encontrado en el escaneo"
    heroe_carol_danvers = "No se encuentra en la base actual"
    
    superheroes_femeninos = []
    personajes_masculinos = []
    datos_con_letra_s = []

    for _ in range(cantidad_elementos):
        dato = cola.attention()
        
        personaje = dato["personaje"].upper()
        superheroe = dato["superheroe"].upper()
        genero = dato["genero"].upper()

        if superheroe == "CAPITANA MARVEL":
            nombre_capitana_marvel = dato["personaje"]

        if genero == "F":
            superheroes_femeninos.append(dato["superheroe"])

        if genero == "M":
            personajes_masculinos.append(dato["personaje"])

        if personaje == "SCOTT LANG":
            heroe_scott_lang = dato["superheroe"]

        if personaje.startswith("S") or superheroe.startswith("S"):
            datos_con_letra_s.append(dato)

        if personaje == "CAROL DANVERS":
            heroe_carol_danvers = dato["superheroe"]

        cola.arrive(dato)

    print("  REPORTE FINAL DE SHIELD ")
    
    print(f"\n[A] Identidad de Capitana Marvel: {nombre_capitana_marvel}")
    
    print(f"\n[B] Superhéroes femeninos encontrados ({len(superheroes_femeninos)}):")
    for heroina in superheroes_femeninos:
        print(f"    - {heroina}")
        
    print(f"\n[C] Personajes masculinos encontrados ({len(personajes_masculinos)}):")
    for chabon in personajes_masculinos:
        print(f"    - {chabon}")
        
    print(f"\n[D] Identidad heroica de Scott Lang: {heroe_scott_lang}")
    
    print(f"\n[E] Registros que comienzan con la letra 'S' ({len(datos_con_letra_s)}):")
    for registro in datos_con_letra_s:
        print(f"    - Personaje: {registro['personaje']} | Héroe: {registro['superheroe']}")
        
    print(f"\n[F] Estado de Carol Danvers: {heroe_carol_danvers}")

def generar_mcu_random(cantidad: int) -> Queue:
    cola_random = Queue()
    
    base_datos = [
        {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
        {"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
        {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
        {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
        {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
        {"personaje": "Peter Parker", "superheroe": "Spider-Man", "genero": "M"},
        {"personaje": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"},
        {"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
        {"personaje": "Bruce Banner", "superheroe": "Hulk", "genero": "M"},
        {"personaje": "Thor Odinson", "superheroe": "Thor", "genero": "M"},
        {"personaje": "Hope van Dyne", "superheroe": "Wasp", "genero": "F"},
        {"personaje": "Sam Wilson", "superheroe": "Falcon", "genero": "M"},
        {"personaje": "Clint Barton", "superheroe": "Hawkeye", "genero": "M"}
    ]
    
    seleccion = random.sample(base_datos, min(cantidad, len(base_datos)))
    
    for p in seleccion:
        cola_random.arrive(p)
        
    return cola_random

def mostrar_cola_actual(cola: Queue, titulo: str):
    cantidad = cola.size()
    print(f"\n {titulo} ({cantidad} personajes en la base actual)")
    for _ in range(cantidad):
        dato = cola.attention()
        print(f"- {dato['personaje']} ({dato['superheroe']}) [{dato['genero']}]")
        cola.arrive(dato)

if __name__ == "__main__":
    cola_mcu = generar_mcu_random(8)
    
    mostrar_cola_actual(cola_mcu, "ESCANEANDO BASE DE DATOS")
    
    reporte_shield_mcu(cola_mcu)