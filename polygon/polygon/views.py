from urllib import response
from attr import attr
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
import os
import uuid


rating_list = [
        'Culture',
        'Diversity',
        'Work-Life Balance',
        'Management',
        'Salary and Benefits',
        'Promotion',
        'Overall',  
    ]

def homePage(request):
    
    return render(request, 'index.html', {'rating_list': rating_list})

def review(request):
    attrs = [
        'organisation',
        'jobtitle',
        'culture',
        'diversity',
        'worklife',
        'management',
        'salary',
        'promotion',
        'overall',
    ]
    if request.POST.get('action') == 'post':
        # do something
        if not os.path.exists('reviews_folder'):
            os.makedirs('reviews_folder')
        data = {}
        for att in attrs:
            data[att] =request.POST.get(att)
        json_data = json.dumps(data)
        uuid.
        return HttpResponse('success')