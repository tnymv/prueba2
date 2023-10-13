from reservacion import views
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r"clientes",views.ClientViewSet, "clientes")
router.register(r"habitacion",views.HabitacionViewSet, "habitacion")
router.register(r"reservacion",views.ReservacionViewSet, "reservacion")

urlpatterns = [
    path(r"", include(router.urls)),
]