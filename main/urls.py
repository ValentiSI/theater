from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='home'),
    path('time/', views.time_view, name='time'),
    path('script/', views.script_view, name='script'),
]
