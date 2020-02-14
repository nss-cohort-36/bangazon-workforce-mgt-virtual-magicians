import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Training
from ..connection import Connection


def get_training(training_id):
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
        where t.id = ?
        """, (training_id,))

        return db_cursor.fetchone()

@login_required
def training_details(request, training_id):
    if request.method == 'GET':
        training = get_training(training_id)

        template = 'trainings/training_details.html'
        context = {
            'training': training
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE hrapp_training
                SET title = ?,
                    start_date = ?,
                    end_date = ?,
                    capacity = ?,
                    description = ?
                WHERE id = ?
                """,
                (
                    form_data['title'], form_data['start_date'],
                    form_data['end_date'], form_data['capacity'],
                    form_data["description"], training_id,
                ))

            return redirect(reverse('hrapp:training_list'))

        # Check if this POST is for deleting a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                    DELETE FROM hrapp_training
                    WHERE id = ?
                """, (training_id,))

            return redirect(reverse('hrapp:training_list'))