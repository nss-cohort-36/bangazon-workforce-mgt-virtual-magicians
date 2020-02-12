import sqlite3
from ..connection import Connection
from django.shortcuts import render
from hrapp.models import Training


def training_list(request):
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
                t.capacity
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

                all_trainings.append(training)

    template = 'trainings/training_list.html'
    context = {
        'trainings': all_trainings
    }

    return render(request, template, context)