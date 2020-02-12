import sqlite3
from django.shortcuts import render
from ...models import Computer
from ..connection import Connection


def computer_form(request):
    if request.method == 'GET':
        template = 'computers/computer_form.html'
        context = {}

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_computer
            (
                make, model, purchase_date
            )
            VALUES (?, ?, ?)
            """,
            (form_data['make'], form_data['model'],
                form_data['purchase_date']))

            return redirect(reverse('hrapp:computers'))