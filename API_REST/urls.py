from django.urls import path, include
from rest_framework import routers
from API_REST import views #accede a dotas las clases disponibles
from .views import * #la definicion de cada funcion

router=routers.DefaultRouter()
router.register(r'Vehiculos', views.VehiculoViewSet) # la R al inicio permite interpretar de manera correcta los endpoints que se van a generar


urlpatterns = [
    path('raiz/', DataViews.as_view(), name='ViewData'),
    path('raiz/<int:id>', DataViews.as_view(), name='Vehiculo_process'),
    path('put_process/', vehiculo_update.as_view(), name='Actualizacion'),
    path('api/', include(router.urls)),
    path('index/', index),
    path('formulario/', formularioP),
    path('agregarVh/', addVh, name='cargar_Vehiculo'),
    path('get/',gettemplate),
    path('put/',putview),
    path('dlview', dlview),
    path('delete_vh/',delete_vehiculos)
   
    
]

