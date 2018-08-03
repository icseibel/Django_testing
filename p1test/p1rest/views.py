from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, MedicineSerializer, MedicineScheduleSerializer
from p1.models import Medicine, MedicineSchedule


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Medicines to be viewed or edited
    """
    queryset = Medicine.objects.all().order_by('name')
    serializer_class = MedicineSerializer

class MedicineScheduleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Medicine Schedule to be viewed or edited
    """
    queryset = MedicineSchedule.objects.all()
    serializer_class = MedicineScheduleSerializer()
