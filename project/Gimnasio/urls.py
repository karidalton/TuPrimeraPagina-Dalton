from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index" ),
    path("sede/list", views.sede_list, name="sede_list" ),
    path("plan/list", views.plan_list, name="plan_list" ),
    path("suscriptor/list", views.suscriptor_list, name="suscriptor_list" ),
    path("suscriptor/form", views.suscriptor_form, name="suscriptor_form" ),
    path("sede/form", views.sede_form, name="sede_form" ),
    path("suscriptor_por_sede/list", views.suscriptor_por_sede, name="suscriptor_por_sede" ),
    path("asignacion_sede/list", views.asignar_sede_form, name="asignacion_sede_form" ),
    
]
