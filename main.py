# gestor_tareas.py

import openai
from autogpt import AutoGPT
from decouple import config

# Configuración de la API key en la librería OpenAI
openai_api_key = config('OPENAI_API_KEY')
openai.api_key = openai_api_key

# Paso 5: Creación de la Lista de Tareas
lista_de_tareas = []

# Paso 6: Creación de una Función de Generación de Tareas con Code Whisperer
def crear_tarea_desde_descripcion(descripcion):
    # Utiliza AutoGPT para generar código basado en la descripción
    codigo_generado = AutoGPT.generate_code(descripcion)
    
    # Agrega la tarea a la lista
    lista_de_tareas.append(codigo_generado)

# Paso 7: Interacción con el Usuario
while True:
    descripcion_tarea = input("Ingresa la descripción de la tarea (o 'salir' para terminar): ")
    
    if descripcion_tarea.lower() == 'salir':
        break
    
    crear_tarea_desde_descripcion(descripcion_tarea)

# Muestra la lista final de tareas
print("Lista de Tareas Generadas:")
for tarea in lista_de_tareas:
    print("- ", tarea)
