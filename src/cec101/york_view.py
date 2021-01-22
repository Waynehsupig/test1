from django.http import HttpResponse
from django.shortcuts import render

def yorkTemplate(request):
    return render(request, 'yorkTemplate.html')

def yorkAction(request):

    context = {
        'word1':"Hello",
        'word2':"!"
    }

    return render(request, 'yorkTemplate.html', context)