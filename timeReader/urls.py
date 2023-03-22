from . import views
from django.urls import path
urlpatterns = [
    path('getget',views.getget,name= 'getget')
]