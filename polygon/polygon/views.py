from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

def get_nft():
    return 1
def homePage(request):
    
    return render(request, 'homepage.html', {'nft': get_nft()})

