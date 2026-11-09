
# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# [169]
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

from tree import BinaryTree

# Datos extraídos de la tabla
datos_criaturas = [
    {"nombre": "Ceto", "derrotado_por": "-"},
    {"nombre": "Tifón", "derrotado_por": "Zeus"},
    {"nombre": "Equidna", "derrotado_por": "Argos Panoptes"},
    {"nombre": "Dino", "derrotado_por": "-"},
    {"nombre": "Pefredo", "derrotado_por": "-"},
    {"nombre": "Enio", "derrotado_por": "-"},
    {"nombre": "Escila", "derrotado_por": "-"},
    {"nombre": "Caribdis", "derrotado_por": "-"},
    {"nombre": "Euríale", "derrotado_por": "-"},
    {"nombre": "Esteno", "derrotado_por": "-"},
    {"nombre": "Medusa", "derrotado_por": "Perseo"},
    {"nombre": "Ladón", "derrotado_por": "Heracles"},
    {"nombre": "Águila del Cáucaso", "derrotado_por": "-"},
    {"nombre": "Quimera", "derrotado_por": "Belerofonte"},
    {"nombre": "Hidra de Lerna", "derrotado_por": "Heracles"},
    {"nombre": "León de Nemea", "derrotado_por": "Heracles"},
    {"nombre": "Esfinge", "derrotado_por": "Edipo"},
    {"nombre": "Dragón de la Cólquida", "derrotado_por": "-"},
    {"nombre": "Cerbero", "derrotado_por": "-"},
    {"nombre": "Cerda de Cromión", "derrotado_por": "Teseo"},
    {"nombre": "Ortro", "derrotado_por": "Heracles"},
    {"nombre": "Toro de Creta", "derrotado_por": "Teseo"},
    {"nombre": "Jabalí de Calidón", "derrotado_por": "Atalanta"},
    {"nombre": "Carcinos", "derrotado_por": "-"},
    {"nombre": "Gerión", "derrotado_por": "Heracles"},
    {"nombre": "Cloto", "derrotado_por": "-"},
    {"nombre": "Láquesis", "derrotado_por": "-"},
    {"nombre": "Átropos", "derrotado_por": "-"},
    {"nombre": "Minotauro de Creta", "derrotado_por": "Teseo"},
    {"nombre": "Harpías", "derrotado_por": "-"},
    {"nombre": "Argos Panoptes", "derrotado_por": "Hermes"},
    {"nombre": "Aves del Estínfalo", "derrotado_por": "-"},
    {"nombre": "Talos", "derrotado_por": "Medea"},
    {"nombre": "Sirenas", "derrotado_por": "-"},
    {"nombre": "Pitón", "derrotado_por": "Apolo"},
    {"nombre": "Cierva de Cerinea", "derrotado_por": "-"},
    {"nombre": "Basilisco", "derrotado_por": "-"},
    {"nombre": "Jabalí de Erimanto", "derrotado_por": "-"}
]

arbol = BinaryTree()

# G.
for criatura in datos_criaturas:
    criatura['descripcion'] = ''
    criatura['capturada'] = ''
    arbol.insert_node(criatura['nombre'], other_value=criatura)

def inorden_a(root):
    if root is not None:
        inorden_a(root.left)
        print(f"Criatura: {root.value} - Derrotado por: {root.other_values['derrotado_por']}")
        inorden_a(root.right)

def contar_derrotas(root, conteo):
    if root is not None:
        contar_derrotas(root.left, conteo)
        heroe = root.other_values['derrotado_por']
        if heroe != '-':
            conteo[heroe] = conteo.get(heroe, 0) + 1
        contar_derrotas(root.right, conteo)

def listar_por_condicion(root, campo, valor, coincidencia_exacta=True):
    if root is not None:
        listar_por_condicion(root.left, campo, valor, coincidencia_exacta)
        if root.other_values[campo] == valor:
            print(f"- {root.value}")
        listar_por_condicion(root.right, campo, valor, coincidencia_exacta)

#A
print("\n Listado inorden")
inorden_a(arbol.root)

#B
print("\n Cargar descripción")
busqueda_desc = input("Ingrese el nombre de la criatura (o presione Enter para omitir): ")
if busqueda_desc:
    nodo_desc = arbol.search(busqueda_desc)
    if nodo_desc:
        nodo_desc.other_values['descripcion'] = input(f"Ingrese la descripción para {nodo_desc.value}: ")
        print("Descripción guardada.")
    else:
        print("Criatura no encontrada.")

#C
print("\n Información de Talos")
nodo_talos = arbol.search('Talos')
if nodo_talos:
    print(f"Nombre: {nodo_talos.value}")
    print(f"Derrotado por: {nodo_talos.other_values['derrotado_por']}")
    print(f"Descripción: {nodo_talos.other_values['descripcion']}")
    print(f"Capturada por: {nodo_talos.other_values['capturada']}")

#D
print("\n Top 3 Héroes/Dioses con más derrotas")
conteo_heroes = {}
contar_derrotas(arbol.root, conteo_heroes)
top_3 = sorted(conteo_heroes.items(), key=lambda x: x[1], reverse=True)[:3]
for i, (heroe, cantidad) in enumerate(top_3, 1):
    print(f"{i}. {heroe}: {cantidad} criaturas")

#E
print("\n Criaturas derrotadas por Heracles")
listar_por_condicion(arbol.root, 'derrotado_por', 'Heracles')

#F
print("\n Criaturas que no han sido derrotadas")
listar_por_condicion(arbol.root, 'derrotado_por', '-')

#H
print("\n Modificando capturas por Heracles")
criaturas_a_capturar = ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto']
for c in criaturas_a_capturar:
    nodo = arbol.search(c)
    if nodo:
        nodo.other_values['capturada'] = 'Heracles'
print("Atrapadas por Heracles actualizadas con éxito.")

#I
print("\n Búsqueda por coincidencia")
palabra = input("Ingrese una palabra o sílaba para buscar en el árbol: ")
arbol.proxy_search(palabra.lower())

#J
print("\n Eliminando a Basilisco y Sirenas")
arbol.delete_node('Basilisco')
arbol.delete_node('Sirenas')
print("Nodos eliminados.")

#K
print("\n Modificando Aves del Estínfalo")
nodo_aves = arbol.search('Aves del Estínfalo')
if nodo_aves:
    nodo_aves.other_values['derrotado_por'] = 'Heracles'
    nodo_aves.other_values['descripcion'] = 'Heracles derrotó a varias de estas aves.'
    print("Aves del Estínfalo actualizadas.")

#L
print("\n Modificando Ladón a Dragón Ladón")
nodo_ladon = arbol.search('Ladón')
if nodo_ladon:
    valor_eliminado, otros_valores_eliminados = arbol.delete_node('Ladón')
    otros_valores_eliminados['nombre'] = 'Dragón Ladón'
    arbol.insert_node('Dragón Ladón', otros_valores_eliminados)
    print("Nombre modificado a Dragón Ladón.")

#M
print("\n Listado del árbol por nivel")
arbol.by_level()

#N
print("\n Criaturas capturadas por Heracles")
listar_por_condicion(arbol.root, 'capturada', 'Heracles')
