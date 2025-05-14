import pandas as pd
import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

CSV_PATH = "../data/Medicinal.csv"

def formatear_especie(nombre):
    partes = nombre.strip().split()
    if len(partes) >= 2:
        return partes[0].capitalize() + " " + partes[1].lower()
    return nombre.capitalize()

@csrf_exempt
def procesar_txt(request):
    if request.method == "POST" and request.FILES.get("archivo"):
        archivo = request.FILES["archivo"]
        contenido = archivo.read().decode("utf-8").strip()
        nombre = formatear_especie(contenido)

        df = pd.read_csv(CSV_PATH)
        df.columns = df.columns.str.strip()
        df['Especie'] = df['Especie'].astype(str).str.strip()

        resultado = df[df['Especie'] == nombre]

        if not resultado.empty:
            lineas = []
            for _, fila in resultado.iterrows():
                lineas.append(f"Familia: {fila['Familia']}")
                lineas.append(f"Estados con ese uso: {fila['Estados con ese uso']}")
                lineas.append("")
            respuesta = "\n".join(lineas)
        else:
            respuesta = "La planta no fue encontrada en la base de datos."

        # Guardar el archivo de respuesta
        ruta_salida = os.path.join(settings.MEDIA_ROOT, "respuesta.txt")
        with open(ruta_salida, "w", encoding="utf-8") as f:
            f.write(respuesta)

        return HttpResponse("Archivo procesado correctamente.", status=200)

    return HttpResponse("Debes enviar un archivo .txt por POST con el campo 'archivo'.", status=400)
