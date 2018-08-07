from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from p1rest import views

urlpatterns = [
    url(r'^schedulebymedicine/$', views.ScheduleByMedicineViewSet.as_view(), name='schedulebymedicine'),
    url(r'^geolocation/$', views.GeoLocationViewSet.as_view(), name='geolocation'),
]

urlpatterns = format_suffix_patterns(urlpatterns)