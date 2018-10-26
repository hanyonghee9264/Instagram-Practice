import mimetypes
import os

from django.http import FileResponse

from config import settings


def media_serve(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    content_type = mimetypes.guess_type(str(file_path))
    return FileResponse(open(file_path, 'rb'), content_type=content_type)
