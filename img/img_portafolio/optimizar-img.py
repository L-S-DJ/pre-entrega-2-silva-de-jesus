import os
from PIL import Image

# Función para optimizar una imagen
def optimizar_imagen(ruta_imagen, calidad=85):
    # Abre la imagen
    imagen = Image.open(ruta_imagen)
    
    # Obtiene la ruta y nombre de archivo
    ruta_directorio, nombre_archivo = os.path.split(ruta_imagen)
    
    # Guarda la imagen optimizada con la misma calidad
    imagen.save(ruta_imagen, optimize=True, quality=calidad)
    print(f"Imagen optimizada: {nombre_archivo}")

# Itera sobre todas las imágenes en la carpeta
def optimizar_imagenes_en_carpeta(carpeta, calidad=85):
    for archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_archivo) and archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            optimizar_imagen(ruta_archivo, calidad)

if __name__ == "__main__":
    # Obtiene la carpeta donde se encuentra el script
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Llama a la función para optimizar imágenes en la carpeta actual
    optimizar_imagenes_en_carpeta(carpeta_actual)
