from . import views
from django.urls import path
urlpatterns = [
    path('getget',views.getget,name= 'getget'),
    path('postpost',views.postpost,name= 'postpost')
]