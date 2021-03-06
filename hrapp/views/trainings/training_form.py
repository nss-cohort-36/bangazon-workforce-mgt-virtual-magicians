import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Training
from .training_details import get_training
from ..connection import Connection


def get_trainings():
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

        return db_cursor.fetchall()

@login_required
def training_form(request):
    if request.method == 'GET':
        trainings = get_trainings()
        template = 'trainings/training_form.html'
        context = {
            'all_trainings': trainings
        }

        return render(request, template, context)
    
@login_required
def training_edit_form(request, training_id):

    if request.method == 'GET':
        training = get_training(training_id)
        trainings = get_trainings()

        template = 'trainings/training_form.html'
        context = {
            'training': training,
            'all_trainings': trainings
        }

        return render(request, template, context)