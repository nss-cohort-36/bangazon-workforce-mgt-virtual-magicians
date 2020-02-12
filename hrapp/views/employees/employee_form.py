import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee
from hrapp.models import Department
# from hrapp.models import model_factory
from ..connection import Connection


def employee_form(request):
    if request.method == 'GET':
        template = 'employees/employee_form.html'
        context = {}

        return render(request, template, context)
