import sqlite3
from django.shortcuts import render
from hrapp.models import department
from ..connection import Connection



def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:            
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()


            db_cursor.execute("""
            select
                d.id,
                d.dept_name,
                d.dept_budget
            from hrapp_department d
            """)

            all_departments = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                department = Department()
                department.id = row['id']
                department.dept_name = row['dept_name']
                department.dept_budget = row['dept_budget']



            all_departments.append(department)
              
    template = 'department/department_list.html'
    context = {
        'department' : all_departments
    }

    return render(request, template, context)