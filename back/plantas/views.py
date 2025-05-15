from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import os

@csrf_exempt
def procesar_txt(request):
    if request.method == 'POST' and request.FILES.get('archivo'):
        archivo = request.FILES['archivo']
        ruta_archivo = os.path.join('media', 'pregunta.txt')
        with default_storage.open(ruta_archivo, 'wb+') as destino:
            for chunk in archivo.chunks():
                destino.write(chunk)

        # Leer contenido del archivo de entrada
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            pregunta = f.read().strip()

        # Procesamiento simulado (puedes conectar tu modelo aquí)
        respuesta = f"La planta {pregunta} tiene propiedades medicinales."

        # Guardar la respuesta en media/respuesta.txt
        ruta_respuesta = os.path.join('media', 'respuesta.txt')
        with open(ruta_respuesta, 'w', encoding='utf-8') as f:
            f.write(respuesta)

        return JsonResponse({'mensaje': 'Archivo procesado correctamente.'})

    return JsonResponse({'error': 'Método no permitido o archivo no enviado.'}, status=400)
