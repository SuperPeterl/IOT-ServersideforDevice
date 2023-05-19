from . import views
from django.urls import path
urlpatterns = [
    path('',views.show,name= ''),
    path('listen',views.listen,name= ''),
]