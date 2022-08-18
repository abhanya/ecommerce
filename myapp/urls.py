from django.urls import path
from . import views

urlpatterns=[
    path('index',views.myapp_index,name='index'),
]