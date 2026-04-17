#EJERCICIO 5 :

def convertir_romano(num: str) -> int:
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    if num == "":
        return 0
        
    if len(num) == 1:
        return valores[num[0]]

    valor_actual = valores[num[0]]
    valor_siguiente = valores[num[1]]
    
    if valor_actual < valor_siguiente:
        return -valor_actual + convertir_romano(num[1:])
    else:
        return valor_actual + convertir_romano(num[1:])
    
print(convertir_romano("XII"))
print(convertir_romano("IX"))
print(convertir_romano("MCMXCIV")) 


#EJERCICIO 22 :

import random 

def usar_la_fuerza(mochila: list, contador: int = 1) -> tuple:
    
    if len(mochila) == 0:
        print(" La mochila está vacía, No hay más objetos que sacar.\n")
        return (False, contador - 1)
    
    objeto_actual = mochila[0]
    print(f" Objeto {contador}: Sacando '{objeto_actual}'.")
    
    if objeto_actual == "sable de luz":
        print(f"Encontré el sable de luz!\n")
        return (True, contador)
    else:
        print(f"Este no es el sable de luz, es solo {objeto_actual}, Dejándolo de lado\n")
        lo_encontro, cant_sacados = usar_la_fuerza(mochila[1:], contador + 1)
        return (lo_encontro, cant_sacados)

print("LA FUERZA TE ACOMPAÑA")

mochila_jedi = ["muñecoDeChewbacca", "comida", "mapa", "elmate", "holocron", "anillo"]

poner_sable = random.choice([True, False])

if poner_sable:
    mochila_jedi.append("sable de luz")

    random.shuffle(mochila_jedi)

print(f"\nContenido de la mochila: {mochila_jedi}\n")
print("El Jedi usa la fuerza para buscar el sable de luz.\n")

resultado = usar_la_fuerza(mochila_jedi)

print("RESULTADO FINAL:")

if resultado[0]:
    print(f"El Jedi encontró el sable de luz después de sacar {resultado[1]} objetos.")
else:
    print(f"El Jedi está hasta las manos porque no encontró el sable de luz...")
    print(f"Tuvo que revisar toda la mochila ({resultado[1]} objetos) y nada")