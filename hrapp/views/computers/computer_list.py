import sqlite3
from django.shortcuts import render
from models import Computer


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

