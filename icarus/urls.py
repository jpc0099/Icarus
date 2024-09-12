from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Tareas.views import TareaViewSet

router = DefaultRouter()
router.register(r'tareas', TareaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Incluir las rutas de la API
]
