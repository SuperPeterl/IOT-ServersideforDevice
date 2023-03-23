from . import views
from django.urls import path
urlpatterns = [
    path('getget',views.getget,name= 'getget'),
    path('postpost',views.postpost,name= 'postpost'),
    path('',views.show,name= ''),
    path('fake',views.fake,name= 'fake'),
]