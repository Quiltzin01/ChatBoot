import pandas as pd
import os

# Función para formatear la especie igual que en tu notebook
def formatear_especie(nombre):
    partes = nombre.strip().split()
    if len(partes) >= 2:
        return partes[0].capitalize() + " " + partes[1].lower()
    return nombre.capitalize()

# Rutas
base_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta de 'back'
data_path = os.path.join(base_dir, '..', 'data', 'Medicinal.csv')
pregunta_path = os.path.join(base_dir, 'media', 'pregunta.txt')
respuesta_path = os.path.join(base_dir, 'media', 'respuesta.txt')

# Leer la base de datos
df = pd.read_csv(data_path)
df['Especie'] = df['Especie'].astype(str).str.strip()

# Leer la especie desde el archivo
with open(pregunta_path, 'r', encoding='utf-8') as f:
    especie = f.read().strip()

# Formatear especie
especie_formateada = formatear_especie(especie)

# Buscar en la base de datos
resultado = df[df['Especie'] == especie_formateada]

# Generar respuesta
if not resultado.empty:
    respuestas = []
    for _, fila in resultado.iterrows():
        familia = fila['Familia']
        estados = fila['Estados con ese uso']
        respuestas.append(f"Familia: {familia}\nEstados con ese uso: {estados}\n")
    output = "\n".join(respuestas)
else:
    output = f"La planta '{especie}' no fue encontrada en la base de datos."

# Guardar respuesta
with open(respuesta_path, 'w', encoding='utf-8') as f:
    f.write(output)

print("Consulta completada. Ver archivo 'respuesta.txt'.")
