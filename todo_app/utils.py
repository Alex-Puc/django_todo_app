from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ValidationError
import os

def resize_image(image, max_width, max_height=None):
    if not image:
        raise ValidationError("No se proporcionó una imagen válida.")

    try:
        img = Image.open(image)
        img = img.convert('RGB')  # Asegura compatibilidad con todos los formatos
    except Exception:
        raise ValidationError("No se pudo abrir la imagen. Verifica si el formato es válido.")

    # Obtener tamaño original
    original_width, original_height = img.size

    # Calcular altura si no se proporciona, manteniendo la proporción
    if max_height is None:
        aspect_ratio = original_height / original_width
        max_height = int(max_width * aspect_ratio)

    # Redimensionar la imagen
    img.thumbnail((max_width, max_height), Image.LANCZOS)  # Reemplaza ANTIALIAS (obsoleto)

    # Obtener extensión y nombre seguro
    file_extension = os.path.splitext(image.name)[-1].lower().replace('.', '')
    filename = os.path.basename(image.name)

    # Mapeo de extensiones a formatos válidos
    format_mapping = {
        'jpg': 'JPEG',
        'jpeg': 'JPEG',
        'png': 'PNG',
    }

    output_format = format_mapping.get(file_extension, 'JPEG')
    mime_type = f'image/{file_extension if file_extension in format_mapping else "jpeg"}'

    # Guardar en buffer de memoria
    buffer = BytesIO()
    img.save(buffer, format=output_format, quality=85)  # 85 recomendado para web
    buffer.seek(0)

    return InMemoryUploadedFile(
        buffer,
        field_name='ImageField',
        name=filename,
        content_type=mime_type,
        size=buffer.getbuffer().nbytes,
        charset=None,
    )