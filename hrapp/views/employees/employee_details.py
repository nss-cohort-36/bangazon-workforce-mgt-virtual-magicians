import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from ..connection import Connection
from ...models import Employee


def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select
                e.id,
                e.first_name,
                e.last_name,
                e.start_date,
                e.is_supervisor,
                e.department_id,
                d.dept_name,
                d.id
            from hrapp_employee e
            JOIN hrapp_department d
            where e.department_id = d.id;
            """)

        return db_cursor.fetchone()

def employee_details(request, employee_id):
    if request.method == 'GET':
        employee = get_employee(employee_id)

        template = 'employees/employee_details.html'
        context = {
            'employee': employee
        }

        return render(request, template, {'employee': employee})