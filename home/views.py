from django.shortcuts import render
from django.http import HttpResponse
from home.models import About, Extra
from datetime import datetime
from django.contrib import messages
from django.db import connection
# Create your views here.
def zero(request):
    return render(request, 'zero.html')


def index(request):
    look_for_table = "show tables"
    create = "create table extra(id int auto_increment primary key, fname varchar(20), lname varchar(20))"
    with connection.cursor() as cursor:
        cursor.execute(look_for_table)
        table_names = tuple(cursor.fetchall())
        print(table_names)
        exists=False
        for columns in table_names:
            if columns[0]=='extra':
                exists=True
                break
        if not exists:
            cursor.execute(create)
    if request.method=="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        insert = "insert into extra (fname, lname) values (%s, %s)"
        with connection.cursor() as cursor:
            cursor.execute(insert, (fname, lname))
        messages.success(request, "Your Information is saved")

        
    return render(request, 'index.html')
    
def home(request):
    return render(request, 'home.html')

def services(request):
    look_for_table = "show tables"
    command = "select name from home_about"
    db_names = None
    with connection.cursor() as cursor:
        cursor.execute(look_for_table)
        print(tuple(cursor.fetchall()))
        cursor.execute(command)
        db_names = tuple(cursor.fetchall())
    print(db_names)
    name1 = db_names[0][0]
    name2 = db_names[1][0]
    return render(request, 'services.html', {'name1':name1, 'name2':name2})

def about(request):
    
    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date = datetime.today()
        command = "insert into home_about(name, phone,email, date) values (%s, %s, %s, %s)"
        with connection.cursor() as cursor:
            cursor.execute(command, (name, phone, email, date))

        messages.success(request, "Your Information is saved")
    
    return render(request, 'about.html')
#https://source.unsplash.com/random/1280x720/?cars