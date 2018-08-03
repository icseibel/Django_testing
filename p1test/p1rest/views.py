from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import UserSerializer, GroupSerializer, MedicineSerializer, MedicineScheduleSerializer, MedicineScheduleFilteredSerializer
from p1.models import Medicine, MedicineSchedule
from p1rest.service import getScheduleByMedicine
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse

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
    serializer_class = MedicineScheduleSerializer

@permission_classes((permissions.IsAuthenticated,))
class ScheduleByMedicineViewSet(APIView):
    def get(self, request):
        """
        API endpoint that allows Medicine Schedule to be viewed
        """
        medicine_id = request.GET.get('medicine_id')
        schedules = getScheduleByMedicine(medicine_id=medicine_id)
        serializer = MedicineScheduleFilteredSerializer(schedules, many=True)
        return Response(serializer.data)
