from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar_sesion, name='inicio'),  # Página de inicio
    path('registro/', views.registro, name='registro'),
    path('catalogo_regiones/', views.RegionesCatalogo, name='CatalogoRegiones'),
    path('catalogo_comunas/<int:region_id>/', views.detalle_comunas, name='catalogo_comunas'),
    path('catalogo_comunas_todas/', views.ComunasCatalogo, name='catalogo_comunas_todas'),
    path('detalle_comuna/<int:comuna_id>/', views.detalle_comuna, name='detalle_comuna'),
    path('detalle_comunas/<int:region_id>/', views.detalle_comunas, name='detalle_comunas'), 
    path('eliminar_comuna/<int:comuna_id>/', views.eliminar_comuna, name='eliminar_comuna'),
    path('crear_comuna/', views.crear_comuna, name='crear_comuna'),
    path('api/provincias/<int:region_id>/', views.obtener_provincias, name='obtener_provincias'),
    path('logout/', views.cerrar_sesion, name='logout'),

]
