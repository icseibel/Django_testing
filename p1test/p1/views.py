from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import UpdateView
from .models import Medicine, MedicineSchedule
import requests

# Create your views here.    
class HomeView(generic.ListView):    
    template_name = 'p1/home.html'
    context_object_name = 'medicines'

    def get_queryset(self):
        return Medicine.objects.all()

def medicine_detail(request, medicine_id):
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    medicine_schedules = MedicineSchedule.objects.filter(medicine = medicine)
    return render(request, 'p1/medicine_detail.html', {'medicine' : medicine, 'medicine_schedules' : medicine_schedules})

class ScheduleDetailView(UpdateView):
    model = MedicineSchedule
    fields = ['frequency', 'isactive', 'start_date', 'time_frame_days']
    template_name = 'p1/schedule_detail.html'

def geoloc(request):
    params={'access_key' : 'dda201aa2ba57d35608fd5c340a1ad02'}
    response = requests.get('http://api.ipstack.com/check',params=params)
    geodata = response.json()
    print(geodata)
    return render(request, 'p1/geoloc.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })
