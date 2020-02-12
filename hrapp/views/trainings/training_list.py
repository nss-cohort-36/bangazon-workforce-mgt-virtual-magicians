import sqlite3
from ..connection import Connection
from django.shortcuts import render, redirect
from hrapp.models import Training
from django.urls import reverse


def training_list(request):
    
    # GET request
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:            
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                t.id,
                t.title,
                t.start_date,
                t.end_date,
                t.capacity,
                t.description
            from hrapp_training t
            """)

            all_trainings = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                training = Training()
                training.id = row['id']
                training.title = row['title']
                training.start_date = row['start_date']
                training.end_date = row['end_date']
                training.capacity = row['capacity']
                training.description = row['description']

                all_trainings.append(training)

        template = 'trainings/training_list.html'
        context = {
            'trainings': all_trainings
        }

        return render(request, template, context)

    # POST request
    elif request.method == 'POST':
        form_data = request.POST
        
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_training
            (
                title, start_date, end_date, capacity, description
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (form_data['title'], form_data['start_date'],
                form_data['end_date'], form_data['capacity'], form_data['description']
            ))

        return redirect(reverse('hrapp:training_list'))
