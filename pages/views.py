from itertools import count
import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import ast
import sqlite3
from .models import usuario



def dashBoard(request):
      

    #Connect to SQLite3 DataBASE
    database = sqlite3.connect("db.sqlite3")
    curr = database.cursor()

    name_attributes = '''SELECT usuario, progresoPorcentual, score, minutosJugados FROM pages_usuario ORDER BY score DESC'''
    register = curr.execute(name_attributes)
    data_progress = []

    

    for x in register:
        data_progress.append([  x[0], x[1], x[2], x[3]])
#--------------------------------------------------INICIO---------------------------------------------
#--------------------------------------------------Query of Score-------------------------------------
    consult_name_score = '''SELECT usuario, score FROM pages_usuario'''


    register2 = curr.execute(consult_name_score)
    query_score = [['Username', 'Score']]

    for x in register2:
        query_score.append([x[0],x[1]])
#--------------------------------------------------FIN---------------------------------------------


#--------------------------------------------------INICIO---------------------------------------------

#--------------------------------------------------QUERY OF SCORE-------------------------------------
    consult_name_progresoPorcentual = '''SELECT usuario, progresoPorcentual FROM pages_usuario'''
    

    register3 = curr.execute(consult_name_progresoPorcentual)
    query_progresoPorcentual = [['Username', 'ProgresoPorcentual']]

    for x in register3:
        query_progresoPorcentual.append([x[0],x[1]])
#--------------------------------------------------FIN---------------------------------------------


#--------------------------------------------------INICIO---------------------------------------------
#--------------------------------------------------QUERY OF MINUTES PLAYED-------------------------------------
    consult_name_minutosjugados = '''SELECT usuario, minutosJugados FROM pages_usuario'''
    

    register4 = curr.execute(consult_name_minutosjugados)
    query_minutosJugados = [['Username', 'MinutosJugados']]

    for x in register4:
        query_minutosJugados.append([x[0],x[1]])
#--------------------------------------------------FIN---------------------------------------------

#A cada query se le asigna un nombre (string) para ser llamado al dashboard para su posterior graficación

    return render(request, 'pages/dashBoard.html', {'values':data_progress, 'score':query_score, 'progress':query_progresoPorcentual, 'minutes':query_minutosJugados})

