# RESTAURANTE

# 1. Recibir como mínimo 50 comandas.

# 2. Elegir platillos de un menú de 5 platillos con un mínimo de 3 pasos para su elaboración. Tomando en cuenta como recurso compartido el horno.

# 3. Enviar a su entrega por medio de un mínimo y mostrarlo en pantalla.

# 5. Generar documento que incluya grafo, calculo de paralelismo y el código.

import threading
import random
import time

menu = {
    "Tacos": ["Cocinar la carne", "Calentar tortillas", "Poner carne a las tortillas"],
    "Flautas": ["Enrollar el taco con su relleno", "Freír el taco", "Poner verduras y salsa"],
    "Enchiladas": ["Pasar la tortilla por la salsa", "Poner a cocinar en aceite la tortilla", "Agregar carne o pollo durante la cocción"],
    "Huevos a la mexicana": ["Cortar jitomate y cebolla para acitronar", "Acitronar los vegetales por 5 minutos", "Añadir los huevos hasta que estén cocidos"],
    "Fajitas de pollo": ["Acitronar cebolla y pimiento morrón", "Cocinar y sazonar pechuga de pollo", "Emplatar las verudas revueltas con el pollo"]
}

lock = threading.Lock()

horno = True

def preparar_platillo(platillo, pasos, num_orden, lock):
    with lock:
        horno = False  
        print("Horno en uso")  
        print(f"Preparando {platillo} de la orden número: {num_orden}...")
        for step in pasos:
            print(f"- {step}")
        print("Horno desocupado")
        print(f"¡{platillo} de la orden número {num_orden} está listo!")
        print("Entregando platillos\n")
        horno = True

def generar_orden(num_orden, lock):
    num_platillos = random.randint(1, 5)
    orden = random.sample(list(menu.keys()), num_platillos)
    
    with lock:
        print(f"Orden {num_orden}: {', '.join(orden)}\n")
    
    threads_platillos = []
    for platillo in orden:
        pasos = menu[platillo]
        if len(pasos) < 3:
            pasos += ["añadir toppings"] * (3 - len(pasos))  # add default pasos if needed
        t = threading.Thread(target=preparar_platillo, args=(platillo, pasos, num_orden, lock))
        threads_platillos.append(t)
        t.start()

    for t in threads_platillos:
        t.join()

threads = []
for i in range(50):
    t = threading.Thread(target=generar_orden, args=(i+1, lock))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
