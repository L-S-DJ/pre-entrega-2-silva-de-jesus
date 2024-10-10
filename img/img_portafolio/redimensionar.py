import os
from PIL import Image

def resize_image(image_path, output_size=(600, 600)):
    try:

        with Image.open(image_path) as img:

            img.thumbnail(output_size)

            img.save(image_path)
            print(f"Imagen {os.path.basename(image_path)} redimensionada correctamente.")
    except Exception as e:
        print(f"Error al procesar la imagen {image_path}: {e}")

def resize_images_in_folder():

    folder_path = os.getcwd()


    for filename in os.listdir(folder_path):

        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(folder_path, filename)
            resize_image(image_path)

if __name__ == "__main__":
    resize_images_in_folder()
