from p1.models import ThirdPartyApiKeys
from datetime import datetime
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
import platform
import requests

class GeoLocation(object):
    def __init__(self, ip, ip_type, country_name, country_code, latitude, longitude, location_time=None):
        self.ip = ip
        self.ip_type = ip_type
        self.country_name = country_name
        self.country_code = country_code
        self.latitude = latitude
        self.longitude = longitude
        self.location_time = location_time or datetime.now()
        self.os = platform.system()
        self.release = platform.release()
        self.version = platform.version()

class GeoLocationSerializer(serializers.Serializer):
    ip = serializers.CharField(max_length=50)
    ip_type = serializers.CharField(max_length=5)
    country_name = serializers.CharField(max_length=50)
    country_code = serializers.CharField(max_length=2)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    location_time = serializers.DateTimeField()
    os = serializers.CharField(max_length=30)
    release = serializers.CharField(max_length=30)
    version = serializers.CharField(max_length=10)

def GeoLocationRequest():
    thirdpartyapi = ThirdPartyApiKeys.objects.get(api_name = 'GeoLoc')
    print(thirdpartyapi)
    params={'access_key' : thirdpartyapi.api_key}    
    #response = requests.get('http://api.ipstack.com/check',params=params)
    response = requests.get(thirdpartyapi.api_url, params=params)
    geodata = response.json()
    geolocation = GeoLocation(ip=geodata['ip'], ip_type=geodata['type'], country_name=geodata['country_name'], 
                    country_code=geodata['country_code'], latitude=geodata['latitude'], longitude=geodata['longitude'])
    serializer = GeoLocationSerializer(geolocation)
    return serializer
