from django.urls import path
from . import views
# from .views import button_view

urlpatterns = [
    path('', views.index, name='index'),
    
]
