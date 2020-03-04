from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from empleados.views import UsuarioViewSet

router = DefaultRouter()
router.register(r'empleados', UsuarioViewSet)  #view para routear a los empleados

urlpatterns = router.urls                    #se guarda la informacion de router en urlpatters, asi se envia la data por ese link

urlpatterns += [
    path('admin/', admin.site.urls),  #url para abrir el link
]
