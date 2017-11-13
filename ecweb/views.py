from django.shortcuts import render
from django.http import HttpResponseRedirect


def ec_home(request):
    return render(request, 'ecweb/home.html')


def ec_board(request):
    if request.user.is_authenticated:
        return render(request, 'ecweb/board.html')
    else:
        return HttpResponseRedirect("/")
