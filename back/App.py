from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import os

# Cargar el CSV una sola vez al iniciar el servidor
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, 'plantas.csv'))
df.columns = df.columns.str.strip()
df['Especie'] = df['Especie'].astype(str).str.strip()

def formatear_especie(nombre):
    partes = nombre.strip().split()
    if len(partes) >= 2:
        return partes[0].capitalize() + " " + partes[1].lower()
    return nombre.capitalize()

def buscar_planta(request):
    especie = request.GET.get('especie', '')
    especie_formateada = formatear_especie(especie)
    resultado = df[df["Especie"] == especie_formateada]

    if not resultado.empty:
        fila = resultado.iloc[0]
        data = {
            "especie": especie_formateada,
            "familia": fila["Familia"],
            "estados_con_uso": fila["Estados con ese uso"]
        }
    else:
        data = {"error": "Planta no encontrada"}

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(data)
    else:
        return render(request, 'buscar.html', data)