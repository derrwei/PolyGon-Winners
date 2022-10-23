from urllib import response
from attr import attr
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
import os
import uuid
import random
import string
from polygon.NFT import *
from polygon.transfer import *

rating_list = [
        'Culture',
        'Diversity',
        'Work-Life Balance',
        'Management',
        'Salary and Benefits',
        'Promotion',
    ]

def homePage(request):
    
    return render(request, 'index.html', {'rating_list': rating_list})

def unique_id(size):
    chars = list(set(string.ascii_uppercase + string.digits).difference('LIO01'))
    return ''.join(random.choices(chars, k=size))

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
        'review',
    ]
    data = {}
    review_data = {"Organization": "Company Name", 
                "Job_Title": "Position", 
                "Ratings": {"Culture": 5, 
                            "Diversity": 5, 
                            "Work_Life_Balance": 5,
                             "Management": 5, 
                             "Salary_Benefits": 5, 
                             "Promotion_Opportunities": 5, 
                             "Overall": 5}, 
            "Reviews": "Company is good!"}
    if request.POST.get('action') == 'post':
        # do something
        if not os.path.exists('reviews_folder'):
            os.makedirs('reviews_folder')
        for att in attrs:
            data[att] =request.POST.get(att)

        review_data['Organization'] = data['organisation']
        review_data['Job_Title'] = data['jobtitle']
        review_data['Ratings']['Culture'] = data['culture']
        review_data['Ratings']['Diversity'] = data['diversity']
        review_data['Ratings']['Work_Life_Balance'] = data['worklife']
        review_data['Ratings']['Management'] = data['management']
        review_data['Ratings']['Salary_Benefits'] = data['salary']
        review_data['Ratings']['Promotion_Opportunities'] = data['promotion']
        review_data['Ratings']['Overall'] = round((int(data['culture'])+ int(data['diversity'])+ int(data['worklife'])+ int(data['management'])+ int(data['salary'])+ int(data['promotion']))/6,2)
        review_data['Reviews'] = data['review']
        json_data = json.dumps(review_data)
        file_name = os.path.join('reviews_folder', unique_id(10)+'.json')
        with open(file_name, 'w') as f:
            f.write(json_data)
        
        ipfs = upload_json(file_name)
        NFT_mint(file_name, ipfs)
        return HttpResponse('success')
    

def demo(request):
    
    return render(request, 'search.html')


def search(request):
    if request.POST.get('action') == 'post':
        import time 
        # do something
        search_data = request.POST.get('key_word')

        result = NFT_collect(search_data) 
        print(result)
        return HttpResponse(result)
        
