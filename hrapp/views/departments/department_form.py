import sqlite3
from django.shortcuts import render
from ..connection import Connection
from django.contrib.auth.decorators import login_required




def new_department():
     with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            COUNT(), 
            d.id, 
            d.dept_name, 
            d.dept_budget, 
            e.id, 
            e.department_id
        FROM hrapp_department d
        INNER JOIN hrapp_employee e
        ON d.id =e.department_id
        GROUP BY e.department_id;
        """)
        return db_cursor.fetchall()

@login_required
def department_form(request):
    if request.method == 'GET':
        departments = new_department()
        template = 'department/department_form.html'
        context = {
            'all_departments': departments
        }
        return render(request, template, context)


        
