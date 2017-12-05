from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from .forms import UserForm
from .models import Calendar, Menssage


def ec_home(request):
    return render(request, 'ecweb/home.html')


@login_required
def ec_board(request):
    return render(request, 'ecweb/board.html')


@login_required
def home_dashboard(request):
    current_user = request.user
    return render(request, 'ecweb/dashboard.html',
                  {'current_user': current_user})


@login_required
def user_detail(request):
    current_user = request.user
    return render(request, 'ecweb/student.html',
                  {'current_user': current_user})



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


@login_required
def calendar_view(request):
    events = Calendar.objects.all()

    return render(request, 'ecweb/calendar.html', {'events': events,
                                                   })
