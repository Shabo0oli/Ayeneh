from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import *
from json import JSONEncoder
from django.contrib.admin.views.decorators import staff_member_required
import json


import random


from .models import *

from openpyxl import load_workbook



from django import forms

from io import BytesIO

class quizForm(forms.Form):
   file = forms.FileField()



@csrf_exempt
def addquiz(request):

    context = {}

    if request.method == "POST":
        quiz = Quiz.objects.get(id = request.POST['quiz'])
        file =request.FILES['file']
        file = file.read()
        wb = load_workbook(filename=BytesIO(file))
        ws = wb['quiz']
        for row in ws.rows:
            question = Question()
            for cell in row:
                if cell.value != None:
                    if cell.col_idx == 1 :
                        question = Question(Quiz=quiz , Text=cell.value)
                        question.save()
                    else :
                        answer = Answer(Question=question , Text=cell.value)
                        answer.save()




        context['status'] = "success"

        return JsonResponse(context, encoder=JSONEncoder)
    else:
        return render(request, 'addquiz.html', context)






@csrf_exempt
def addkey(request):

    context = {}

    if request.method == "POST":
        quiz = Quiz.objects.get(id = request.POST['quiz'])
        file =request.FILES['file']
        file = file.read()
        wb = load_workbook(filename=BytesIO(file))
        ws = wb['quiz']
        for row in ws.rows:
            question = Question()
            answer = Answer()
            for cell in row:
                if cell.value!= None :
                    if  cell.row == 1 :
                        continue
                    elif cell.col_idx == 1:
                        question = Question.objects.get(Number = cell.value , Quiz = quiz)
                    elif cell.col_idx ==2 :
                        answer = Answer.objects.get(Number = cell.value , Question=question)
                    else :
                        assessment = Assessment(Answer=answer ,Value=cell.value , Parameter=Parameter.objects.get(Name=
                                                                                                 ws.cell(column=cell.col_idx ,row=1).value  , Quiz=quiz))
                        assessment.save()





        context['status'] = "success"

        return JsonResponse(context, encoder=JSONEncoder)
    else:
        return render(request, 'addkey.html', context)
