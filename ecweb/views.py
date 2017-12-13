from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import date

from django.contrib.auth import logout

from .forms import PhotoForm
from .models import Calendar, Menssage, User


@login_required
def home_dashboard(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    date_start = user.date_joined.date()
    days_con = date.today() - date_start
    days_cont_int = int(days_con.days)
    if user.type_of_course == "1-month":
        count_day = 30 - days_cont_int
        percent = int(-100.0 * (count_day / 30))

    else:
        count_day = 30 * 6 - days_cont_int
        percent = int(100.0 * (count_day / (30 * 6)))

    return render(request, 'ecweb/dashboard.html',
                  {'current_user': current_user, 'days_cont_int': days_cont_int})


@login_required
def user_detail(request):
    current_user = request.user
    insta = get_object_or_404(User, pk=int(current_user.id))
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=insta)
        if form.is_valid():
            profil = form.save()
            profil.user = current_user
            profil.save()

            return redirect('user_detail')
    else:
        form = PhotoForm()
    return render(request, 'ecweb/student.html',
                  {'current_user': current_user, 'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')


@login_required
def calendar_view(request):
    events = Calendar.objects.all()
    return render(request, 'ecweb/calendar.html', {'events': events})


@login_required
def classroom_view(request):
    current_user = request.user
    return render(request, 'ecweb/classroom.html', {'current_user': current_user, })
