import random
import time

# Códigos de color ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

# Función para limpiar la pantalla por completo
def limpiar_pantalla():
    print("\033[H\033[J", end="")

# Lista amplia de animales para elegir 10 al azar
lista_animales_global = [
    "Perro", "Gato", "Loro", "Dragón", "Capibara", "Hurón", "Hámster", 
    "Conejo", "Tortuga", "Iguana", "Zorro", "Panda", "Mapache", "Búho", 
    "Koala", "Erizos", "Chinchilla", "Serpiente", "Camaleón", "Axolote"
]

# Banco de nombres reales
nombres_reales = [
    "Jax", "Bruno", "Milo", "Rocky", "Toby", "Simba", "Leo", "Coco", 
    "Sasha", "Kira", "Luna", "Nala", "Maya", "Rocco", "Dexter", "Ollie", 
    "Boby", "Nico", "Otto", "Sam", "Enzo", "Max", "Lucas", "Mateo"
]

# Banco de nombres ficticios / fantásticos
nombres_ficticios = [
    "Zeus", "Thor", "Loki", "Ragnar", "Vortex", "Nebula", "Azazel", "Goku", 
    "Bender", "Kaiser", "Dante", "Draco", "Kratos", "Shadow", "Venom", "Titan", 
    "Sauron", "Anubis", "Vader", "Zero", "Odin", "Gollum", "Pixel", "Cyber"
]

while True:
    limpiar_pantalla()  # Borra todo lo anterior al volver al menú
    
    animales_menu = random.sample(lista_animales_global, 10)
    opciones_dict = {str(i + 1): animales_menu[i] for i in range(10)}

    print(f"{RED}========================================{RESET}")
    print(f"{BOLD}{RED}     GENERADOR DE APODOS PARA ANIMALES  {RESET}")
    print(f"{RED}========================================{RESET}")
    
    for num, nombre_animal in opciones_dict.items():
        print(f"{YELLOW}{num}){RESET} {CYAN}{nombre_animal}{RESET}")
        
    print(f"{YELLOW}11){RESET} {CYAN}Personalizado (Manual){RESET}")
    print(f"{RED}12) Salir{RESET}")
    print(f"{RED}========================================{RESET}")

    opcion = input(f"\n{BOLD}{BLUE}Ingresa una opción (1-12): {RESET}").strip()

    if opcion in opciones_dict:
        animal = opciones_dict[opcion]
    elif opcion == "11":
        animal = input(f"{YELLOW}Escribe el tipo de animal: {RESET}").strip().capitalize()
        if not animal:
            animal = "Mascota"
    elif opcion == "12" or opcion.lower() == "quit":
        limpiar_pantalla()
        print(f"\n{RED}👋 ¡Hasta luego!{RESET}\n")
        break
    else:
        print(f"\n{RED}❌ Opción no válida. Intenta de nuevo.{RESET}")
        time.sleep(1)
        continue

    # Limpia la pantalla antes de mostrar los nuevos apodos
    limpiar_pantalla()

    # Selecciona 5 reales y 5 ficticios sin repetir
    reales_elegidos = random.sample(nombres_reales, 5)
    ficticios_elegidos = random.sample(nombres_ficticios, 5)

    print(f"{BLUE}🚀 Generando apodos para {BOLD}{YELLOW}{animal}{RESET}{BLUE}...\n{RESET}")

    # Bloque 1: 5 Nombres Reales en VERDE
    print(f"{BOLD}{GREEN}--- 5 APODOS REALES ---{RESET}")
    for i, nombre in enumerate(reales_elegidos, 1):
        print(f"{GREEN}{i}. {nombre} ({animal}){RESET}")
        time.sleep(0.15)

    time.sleep(0.3)

    # Bloque 2: 5 Nombres Ficticios en MAGENTA
    print(f"\n{BOLD}{MAGENTA}--- 5 APODOS FICTICIOS ---{RESET}")
    for i, nombre in enumerate(ficticios_elegidos, 6):
        print(f"{MAGENTA}{i}. {nombre} ({animal}){RESET}")
        time.sleep(0.15)

    print(f"\n{CYAN}✅ ¡Listo! Se mostraron los 10 apodos para {animal}.{RESET}")
    
    # Prompt de salida / reinicio
    respuesta = input(f"\n{YELLOW}Presiona ENTER para volver o escribe '{RED}quit{YELLOW}' para salir: {RESET}").strip().lower()
    
    if respuesta == "quit":
        limpiar_pantalla()
        print(f"\n{RED}👋 ¡Hasta luego!{RESET}\n")
        break