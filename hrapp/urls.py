from django.urls import path
from django.conf.urls import include
from django.contrib.auth.urls import *
from hrapp import views
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('trainings/', training_list, name='training_list'),
]
