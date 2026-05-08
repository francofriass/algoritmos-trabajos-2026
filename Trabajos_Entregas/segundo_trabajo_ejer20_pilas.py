from stacks import Stack

pila_ida = Stack()
direcciones_opuestas = {
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "suroeste": "noreste",
    "noroeste": "sureste",
    "sureste": "noroeste"
}

print ("robot, de ida")
print  ("Escriba 'fin' en la dirección para iniciar el retorno")

while True:
    direccion = input("Ingrese dirección: ")
    if direccion == "fin":
        break
    
    pasos = int(input("Ingrese cantidad de pasos: "))
    movimiento = (direccion, pasos)
    pila_ida.push(movimiento)
    
print ("robot, de vuelta")

while pila_ida.size() > 0:
    direccion, pasos = pila_ida.pop()
    direccion_vuelta = direcciones_opuestas[direccion]
    
    print (f"Mover {pasos} pasos hacia el {direccion_vuelta}")