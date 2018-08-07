from django.contrib.auth.models import User, Group
from rest_framework import serializers
from p1.models import Medicine, MedicineSchedule, ThirdPartyApiKeys


class UserSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Group
        fields = ('url', 'name')

class MedicineSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Medicine
        fields = ('url', 'id', 'name', 'activeIngredient', 'laboratory')

class MedicineScheduleSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = MedicineSchedule
        fields = ('url', 'medicine', 'frequency', 'isactive', 'start_date', 'time_frame_days')

class MedicineScheduleFilteredSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineSchedule
        fields = ('medicine', 'frequency', 'isactive', 'start_date', 'time_frame_days') 

class ThirdPartyApiKeysSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = ThirdPartyApiKeys
        fields = ('url', 'api_name', 'api_url', 'api_key')        