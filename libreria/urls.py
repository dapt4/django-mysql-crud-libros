from django.urls import path
from .views import inicio, nosotros, libros, crear, editar, delete

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', inicio, name="inicio"),
    path('nosotros', nosotros, name="nosotros"),
    path('libros', libros, name="libros"),
    path('libros/crear', crear, name="crear"),
    path('libros/editar', editar, name="editar"),
    path('eliminar/<int:libro_id>', delete, name="eliminar"),
    path('libros/editar/<int:libro_id>', editar, name="editar")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
