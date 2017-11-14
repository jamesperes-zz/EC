from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def ec_home(request):
    return render(request, 'ecweb/home.html')


@login_required
def ec_board(request):
    return render(request, 'ecweb/board.html')
