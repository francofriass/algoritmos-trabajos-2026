import random
from stacks import Stack

def analizar_mcu(pila: Stack):
    pila_aux = Stack()
    
    posicion_actual = 1
    pos_rocket = None
    pos_groot = None
    pelis_viuda = None
        
    print("inicio de la busqueda del MCU\n")

    while pila.size() > 0:
        personaje = pila.pop()
        nombre = personaje["nombre"]
        pelis = personaje["peliculas"]
        
        # a)
        if nombre == "Rocket Raccoon":
            pos_rocket = posicion_actual
        elif nombre == "Groot":
            pos_groot = posicion_actual
                
        # b)
        if pelis > 5:
            print(f"[Punto B] {nombre} tiene más de 5 películas (Total: {pelis})")
                
        # c)
        if nombre in ["Viuda Negra", "Black Widow"]:
            pelis_viuda = pelis
                
        # d)
        primera_letra = nombre[0].upper()
        if primera_letra in ['C', 'D', 'G']:
            print(f"[Punto D] Personaje que inicia con {primera_letra}: {nombre}")
                
        pila_aux.push(personaje)
        posicion_actual += 1
            
    # -------------------------------
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
            
    print("\n Resultado: ")
    if pos_rocket is not None:
        print(f"[Punto A] Rocket Raccoon está en la posición {pos_rocket}")
    else:
        print("[Punto A] Rocket Raccoon no está en la pila.")
            
    if pos_groot is not None:
        print(f"[Punto A] Groot está en la posición {pos_groot}")
            
    if pelis_viuda is not None:
        print(f"[Punto C] Viuda Negra participó en {pelis_viuda} películas.")

def generar_pila_mcu_aleatoria(cantidad: int) -> Stack:
    
    pila = Stack()
    
    nombres_posibles = [
        "Rocket Raccoon", "Groot", "Viuda Negra", "Black Widow", 
        "Capitán América", "Doctor Strange", "Gamora", "Iron Man", 
        "Thor", "Hulk", "Spider-Man", "Daredevil", "Cyclops", 
        "Ant-Man", "Wolverine", "Deadpool"
    ]
    
    cantidad_segura = min(cantidad, len(nombres_posibles))
    nombres_elegidos = random.sample(nombres_posibles, cantidad_segura)
    
    for nombre in nombres_elegidos:
        pelis_al_azar = random.randint(1, 12)
        pila.push({"nombre": nombre, "peliculas": pelis_al_azar})
        
    return pila

if __name__ == "__main__":
    cantidad_a_generar = 8 
    
    print(f" Generando pila de {cantidad_a_generar} personajes aleatorios \n")
    pila_marvel_test = generar_pila_mcu_aleatoria(cantidad_a_generar)
    
    analizar_mcu(pila_marvel_test)