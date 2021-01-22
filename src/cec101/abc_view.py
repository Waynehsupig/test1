from django.http import HttpResponse
from django.shortcuts import render

def abcTemplate(request):
    return render(request, 'abcTemplate.html')

def abcAction(request):

    context = {
        'word1':"Hello",
        'word2':"!"
    }

    return render(request, 'abcTemplate.html', context)