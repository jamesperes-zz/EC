from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth import logout


def ec_home(request):
    return render(request, 'ecweb/home.html')


@login_required
def ec_board(request):
    return render(request, 'ecweb/board.html')


def register(request):

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')

