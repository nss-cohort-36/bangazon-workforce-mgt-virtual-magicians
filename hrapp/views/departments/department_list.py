import sqlite3
from django.shortcuts import render,redirect
from hrapp.models import Department
from ..connection import Connection
from hrapp.models.employee import Employee
from django.db.models import Count
from django.urls import reverse


def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT 
                COUNT(d.id) AS assiged_employee, 
                d.dept_name, 
                d.dept_budget, 
                e.id, 
                e.department_id
            FROM hrapp_department d
            INNER JOIN hrapp_employee e
            ON d.id =e.department_id
            GROUP BY e.department_id;
            """)
            all_departments = []
            dataset = db_cursor.fetchall()


            for row in dataset:
                department = Department()
                department.id = row['id']
                department.dept_name = row['dept_name']
                department.dept_budget = row['dept_budget']
                department.department_id = row['department_id']
                department.assiged_employee = row['assiged_employee']
                all_departments.append(department)

        template = 'department/department_list.html'
        context = {
            'departments': all_departments
        }

        return render(request, template, context)



    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_department 
            (
                dept_name, dept_budget
            )
            VALUES (?, ?)
            """,
            (form_data['dept_name'], form_data['dept_budget']))

        return redirect(reverse('hrapp:department_list'))
