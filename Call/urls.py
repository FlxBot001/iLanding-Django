from django.urls import path
from . import views

app_name = "Call"
urlpatterns = [
   path('', views.home, name="home")
]