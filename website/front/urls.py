# front app urls

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('gallery/',views.gallery,name='gallery'),
    path('generic/',views.generic,name='generic'),
]