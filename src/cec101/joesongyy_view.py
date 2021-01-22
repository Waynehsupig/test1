from django.http import HttpResponse
from django.shortcuts import render

def jTemplate(request):
    return render(request, 'joesongyyTemplate.html')


def joeAction(request):

    context = {
        'word1':"Hello",
        'word2':"!"
    }

    return render(request, 'joesongyyTemplate.html', context)