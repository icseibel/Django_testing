from django.urls import path

from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('<int:medicine_id>/',views.medicine_detail, name='medicine_detail'),
    path('<int:pk>/schedule_detail/',views.ScheduleDetailView.as_view(), name='schedule_detail'),
    path('geoloc/',views.geoloc, name='geoloc'),
]
