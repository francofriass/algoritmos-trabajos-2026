import random
from cola import Queue
from stacks import Stack 

def eliminar_facebook(cola: Queue):
    cantidad_elementos = cola.size()
    print("\n[A] Eliminando notificaciones de Facebook...")
    
    for _ in range(cantidad_elementos):
        notificacion = cola.attention()
        if notificacion["app"].upper() != "FACEBOOK":
            cola.arrive(notificacion)

def mostrar_twitter_python(cola: Queue):
    cantidad_elementos = cola.size()
    print("\n[B] Buscando menciones de Python en Twitter...")
    
    for _ in range(cantidad_elementos):
        notificacion = cola.attention()
        
        es_twitter = notificacion["app"].upper() == "TWITTER"
        tiene_python = "PYTHON" in notificacion["mensaje"].upper()
        
        if es_twitter and tiene_python:
            print(f" -> [{notificacion['hora']}] {notificacion['mensaje']}")
            
        cola.arrive(notificacion)

def contar_rango_horario(cola: Queue):
    pila_temporal = Stack()
    cantidad_elementos = cola.size()
    
    for _ in range(cantidad_elementos):
        notificacion = cola.attention()
        hora = notificacion["hora"]
        
        if "11:43" <= hora <= "15:57":
            pila_temporal.push(notificacion)
            
        cola.arrive(notificacion)
        
    cantidad = pila_temporal.size()
    print(f"\n[C] Se encontraron {cantidad} notificaciones entre las 11:43 y las 15:57.")

def generar_notificaciones_aleatorias(cantidad: int) -> Queue:
    cola_random = Queue()
    
    apps_posibles = ["Facebook", "Twitter", "Instagram", "WhatsApp", "TikTok"]
    
    mensajes_twitter = [
        "estudiando Python para el TP",
        "qué frío hace hoy",
        "no me compila el código en python",
        "salió la nueva película en el cine",
        "el mate con o sin montañita?"
    ]
    
    mensajes_facebook = [
        "alguien le dio like a tu foto",
        "tienes 5 nuevas solicitudes de amistad",
        "hoy es el cumpleaños de vanesa",
        "recuerdo de hace 2 años"
    ]
    
    mensajes_genericos = [
        "Nuevo mensaje recibido",
        "Actualización disponible",
        "Alguien vio tu perfil",
        "Te han etiquetado en un comentario"
    ]
    
    for _ in range(cantidad):
        hora = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"
        app = random.choice(apps_posibles)
        
        if app == "Twitter":
            mensaje = random.choice(mensajes_twitter)
        elif app == "Facebook":
            mensaje = random.choice(mensajes_facebook)
        else:
            mensaje = random.choice(mensajes_genericos)
            
        cola_random.arrive({"hora": hora, "app": app, "mensaje": mensaje})
        
    return cola_random

def mostrar_cola_actual(cola: Queue, titulo: str):
    cantidad = cola.size()
    print(f"\n--- {titulo} ({cantidad} notificaciones) ---")
    for _ in range(cantidad):
        noti = cola.attention()
        print(f"[{noti['hora']}] {noti['app']}: {noti['mensaje']}")
        cola.arrive(noti)

if __name__ == "__main__":
    cola_celular = generar_notificaciones_aleatorias(15)
    
    mostrar_cola_actual(cola_celular, "ESTADO ORIGINAL DEL CELULAR")
    
    eliminar_facebook(cola_celular)
    mostrar_twitter_python(cola_celular)
    contar_rango_horario(cola_celular)
    
    mostrar_cola_actual(cola_celular, "ESTADO FINAL (SIN FACEBOOK)")