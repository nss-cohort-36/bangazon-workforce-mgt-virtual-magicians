import sqlite3
from django.shortcuts import render
from hrapp.models import Department
from ..connection import Connection
from hrapp.models.employee import Employee


def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT 
                d.id, 
                d.dept_name, 
                d.dept_budget, 
                e.id, 
                e.department_id, 
                e.first_name, 
                e.last_name
            FROM hrapp_department d
            INNER JOIN hrapp_employee e
            ON d.id =e.department_id;
            """)
            all_departments = []
            dataset = db_cursor.fetchall()


            for row in dataset:
                department = Department()
                department.id = row['id']
                department.dept_name = row['dept_name']
                department.dept_budget = row['dept_budget']
                department.department_id = row['department_id']
                all_departments.append(department)

    template = 'department/department_list.html'
    context = {
        'departments': all_departments
    }

    return render(request, template, context)
