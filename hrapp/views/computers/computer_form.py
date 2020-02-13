import sqlite3
from django.shortcuts import render
from ...models import Computer
from ..connection import Connection


def computer_form(request):
    if request.method == 'GET':
        template = 'computers/computer_form.html'
        context = {}

        return render(request, template, context)

    