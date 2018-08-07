from django.db import models
from datetime import datetime, timedelta
from django.urls import reverse
from django_cryptography.fields import encrypt

# Create your models here.
class Medicine(models.Model):    			
		name = models.CharField(max_length=30)
		activeIngredient = models.CharField(max_length=80)
		laboratory = models.CharField(max_length=100)
		def __str__(self):
    			return self.name

class MedicineSchedule(models.Model):    	
		FREQUENCY = (
			('24', '24 hours'),
			('12', '12 hours'),
			('8', '8 hours'),
			('6', '6 hours'),
			('4', '4 hours'),
			('2', '2 hours')
		)
		medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
		frequency = models.CharField(max_length=2, choices=FREQUENCY)
		isactive = models.BooleanField(default=True)
		start_date = models.DateField()
		time_frame_days = models.IntegerField()

		def getDueDate(self):
    			return self.start_date + timedelta(days=self.time_frame_days)

		def get_absolute_url(self):
    			return reverse('schedule_detail', kwargs={'pk': self.pk})

class ThirdPartyApiKeys(models.Model):
		api_name = models.CharField(max_length=30)
		api_url = models.CharField(max_length=100)
		api_key = encrypt(models.CharField(max_length=100))
