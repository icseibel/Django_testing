from django.contrib import admin
from .models import Medicine
from .models import MedicineSchedule

# Register your models here.
admin.site.register(Medicine)
admin.site.register(MedicineSchedule)
