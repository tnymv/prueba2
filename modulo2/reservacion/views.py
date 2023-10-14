"""Circle views."""
from logica import logica
# Django REST Framework
from rest_framework import mixins, viewsets

# serializers
from .serializers import ClienteSerializer, HabitacionSerializer, ReservacionSerializer

# Models
from .models import Cliente, Habitacion,Reservacion


# class CircleViewSet(viewsets.ModelViewSet):
class ClientViewSet(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Circle view set."""

    serializer_class = ClienteSerializer
    # permission_classes = (IsAuthenticated,)
    #lookup_field = 'slug_name'

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Cliente.objects.all()
        return queryset
    
    

# class CircleViewSet(viewsets.ModelViewSet):
class HabitacionViewSet(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Circle view set."""

    serializer_class =  HabitacionSerializer
    # permission_classes = (IsAuthenticated,)
    #lookup_field = 'slug_name'

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Habitacion.objects.all()
        return queryset

# class CircleViewSet(viewsets.ModelViewSet):
class HabitacionViewSet(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Circle view set."""

    serializer_class =  HabitacionSerializer
    # permission_classes = (IsAuthenticated,)
    #lookup_field = 'slug_name'

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Habitacion.objects.all()
        return queryset
    

# class CircleViewSet(viewsets.ModelViewSet):
class ReservacionViewSet(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Circle view set."""

    serializer_class =  ReservacionSerializer
    # permission_classes = (IsAuthenticated,)
    #lookup_field = 'slug_name'

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Reservacion.objects.all()
        return queryset
    
