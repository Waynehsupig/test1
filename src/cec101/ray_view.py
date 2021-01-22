from django.http import HttpResponse
from django.shortcuts import render

def rayTemplate(request):
    return render(request, 'rayTemplate.html')

def rayAction(request):

    context = {
        'word1':"Hello",
        'word2':"!"
    }

    return render(request, 'rayTemplate.html', context)