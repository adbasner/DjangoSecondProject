from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>Stomething</em>")

def help(request):
    my_dict = {'help_me': 'I need to go.'}
    return render(request, 'second_app/help.html', context = my_dict)
