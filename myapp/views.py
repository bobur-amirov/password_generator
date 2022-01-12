from django.shortcuts import render
import random

def home(request):
    return render(request, 'home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()?><:;'))

    length = int(request.GET.get("length"))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'password.html', {"password":thepassword})
