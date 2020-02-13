import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee
from hrapp.models import Department
# from hrapp.models import model_factory
from ..connection import Connection


def get_departments():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            d.id,
            d.dept_name
        from hrapp_department d
        """)

        return db_cursor.fetchall()

def employee_form(request):
    if request.method == 'GET':
        department = get_departments()
        template = 'employees/employee_form.html'
        context = {
            'all_departments': department
        }

        return render(request, template, context)
