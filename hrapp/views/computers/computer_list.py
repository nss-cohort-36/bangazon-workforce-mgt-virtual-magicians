import sqlite3
from django.shortcuts import render
from models import Computer
from ..connection import Connection


def computer_list(request):
    if request.method == 'GET'
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                c.make,
                c.purchase_date,
                c.decomission_date
            from hrapp_computer c
            """)

            all_computers = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                computer = Computer()
                computer.id = row['id']
                computer.make = make['make']
                computer.purchase_date = purchase_date['purchase_date']
                computer.decomission_date = decomission_date['decomission_date']

                all_computers.append(computer)

        template = 'computers/computer_list.html'
        context = {
            'all_computers': all_computers
        }

        return render(request, template, context)