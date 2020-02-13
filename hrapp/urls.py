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
    path('departments/', department_list, name='department_list'),
    path('computers/', computer_list, name='computer_list'),
    path('trainings/', training_list, name='training_list'),
    path('computer/form', computer_form, name='computer_form'),
    path('training/form', training_form, name='training_form'),
    path('computers/<int:computer_id>/', computer_details, name='computer'),
    path('trainings/<int:training_id>/', training_details, name='training_details')
]
