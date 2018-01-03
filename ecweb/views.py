from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse as r
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import date
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth import logout
from .forms import PhotoForm, AttendanceForm, CreateUserForm, StudentForm
from .models import ClassRoom, Teacher, Student, Class, BasicUser, Coordinator



@login_required
def create_user_type_view(request, user_type):
    template_name = 'registration/create_user.html'
    types = ('coordinator', 'teacher')
    current_user = request.user
    if user_type not in types:
        raise Http404
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user_type == 'coordinator':
                Coordinator.objects.create(user=user)
            elif user_type == 'teacher':
                Teacher.objects.create(user=user)
            return redirect(r('home_dashboard'))
    else:
        form = CreateUserForm()
    context = {'form': form,
               'current_user': current_user}
    return render(request, template_name, context)


@login_required
def create_student_view(request):
    template_name = 'registration/create_student.html'
    current_user = request.user
    if request.method == 'POST':
        userform = CreateUserForm(request.POST)
        studentform = StudentForm(request.POST)
        if userform.is_valid() and studentform.is_valid():
            user = userform.save()
            student = studentform.save(commit=False)
            student.user = user
            student.save()
            return redirect(r('home_dashboard'))
    else:
        userform = CreateUserForm()
        studentform = StudentForm()
    context = {
        'userform': userform,
        'studentform': studentform,
        'current_user': current_user
    }
    return render(request, template_name, context)

  
@login_required
def home_dashboard(request):
    current_user = request.user
    user = Coordinator.objects.filter(user__id=current_user.id)

    if user:
        return render(request, 'ecweb/coordinator-dashboard.html',
                      {'coordinator': user.first(),
                       'current_user': current_user})

    user = Teacher.objects.filter(user__id=current_user.id)
    if user:
        return render(request, 'ecweb/teacher-dashboard.html',
                      {'teacher': user.first(),
                       'current_user': current_user})

    user = Student.objects.filter(user__id=current_user.id)
    if user:
        date_start = current_user.date_joined.date()
        days_con = date.today() - date_start
        days_cont_int = int(days_con.days)
        if user[0].type_of_course == "1-month":
            count_day = 30 - days_cont_int
            percent = int(-100.0 * (count_day / 30))

        else:
            count_day = 30 * 6 - days_cont_int
            percent = int(100.0 * (count_day / (30 * 6)))

        return render(request, 'ecweb/student-dashboard.html',
                      {'student': user.first(),
                       'current_user': current_user,
                       'days_cont_int': days_cont_int})

    raise Http404


@login_required
def user_detail(request):
    current_user = request.user
    insta = get_object_or_404(BasicUser, pk=int(current_user.id))

    if request.method == 'POST':
        if "change_password" in request.POST:

            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(
                    request, 'Your password was successfully updated!')
                return redirect('user_detail')
            else:
                form = PasswordChangeForm(request.user)
                return render(request, 'ecweb/student.html', {
                    'form': form
                })

        else:

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


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change-password.html', {
        'form': form
    })



def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')


@login_required
def calendar_view(request):
    events = Calendar.objects.all()
    return render(request, 'ecweb/calendar.html', {'events': events})


class ClassRoomListView(LoginRequiredMixin, ListView):

    model = ClassRoom
    template_name = 'ecweb/classroom/classroom.html'

    def get_queryset(self):
        current_user = self.request.user

        queryset = super(ClassRoomListView, self).get_queryset()

        if current_user.is_staff:
            teacher = Teacher.objects.filter(user=current_user.id)

            if teacher.exists():
                queryset = ClassRoom.objects.filter(
                    teachers=teacher.first().id,
                    is_active=True
                )

            else:
                queryset = ClassRoom.objects.filter(is_active=True)

        else:
            student = Student.objects.get(user=current_user.id)
            queryset = ClassRoom.objects.filter(students=student.id, is_active=True)

        return queryset

class ClassRoomDetailView(DetailView):
    model = ClassRoom
    template_name = 'ecweb/classroom/detail_classroom.html'
    queryset = ClassRoom.objects.filter(is_active=True)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        classroom = self.get_object()
        user = request.user

        is_coordinator = Coordinator.objects.filter(user=user).exists()
        student_in_classroom = classroom.students.all().filter(user=user).exists()
        teacher_in_classroom = classroom.teachers.all().filter(user=user).exists()

        if not (student_in_classroom or teacher_in_classroom or is_coordinator):
            return redirect('classroom_view')

        if not classroom.is_active:
            return redirect('classroom_view')

        return super(ClassRoomDetailView, self).dispatch(request, *args, **kwargs)

class ClassRoomCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ClassRoom
    template_name = 'ecweb/classroom/create_classroom.html'
    success_url = reverse_lazy('classroom_view')
    permission_required = 'ecweb.view_all_classrooms'
    fields = (
        'number_class',
        'level',
        'students',
        'teachers',
        'turn'
    )

    def form_valid(self, form):

        self.object = form.save(commit=False)

        classroom_exists = ClassRoom.objects.filter(
            number_class=self.object.number_class,
            level=self.object.level,
            turn=self.object.turn,
            is_active=True
        ).exists()

        if classroom_exists:
            messages.error(
                self.request,
                'This classroom already exists.'
            )
            return super(ClassRoomCreateView, self).form_invalid(form)

        return super(ClassRoomCreateView, self).form_valid(form)

class ClassRoomUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ClassRoom
    template_name = 'ecweb/classroom/update_classroom.html'
    permission_required = 'ecweb.view_all_classrooms'
    fields = (
        'number_class',
        'level',
        'students',
        'teachers',
        'turn'
    )

    def form_valid(self, form):

        self.object = form.save(commit=False)
        form_changed = form.has_changed()

        if form_changed:
            classroom_exists = ClassRoom.objects.filter(
                number_class=self.object.number_class,
                level=self.object.level,
                turn=self.object.turn,
                is_active=True
            ).exclude(pk=self.object.pk).exists()

            if classroom_exists:
                messages.error(
                    self.request,
                    'This classroom already exists.'
                )
                return super(ClassRoomUpdateView, self).form_invalid(form)
            else:
                messages.success(
                    self.request,
                    'Classroom successfully updated'
                )

                return super(ClassRoomUpdateView, self).form_valid(form)

        messages.info(
            self.request,
            'The classroom does changed.'
        )
        return super(ClassRoomUpdateView, self).form_valid(form)

class ClassRoomDeactivateView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ClassRoom
    template_name = 'ecweb/classroom/classroom_confirm_delete.html'
    success_url = reverse_lazy('classroom_view')
    permission_required = 'ecweb.view_all_classrooms'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(success_url)

@login_required
def list_classes_view(request, class_room_id):

    current_user = request.user
    user = Coordinator.objects.filter(user__id=current_user.id)
    if user:
        all_classes = Class.objects.filter(classroom=class_room_id)

    user = Teacher.objects.filter(user__id=current_user.id)
    if user:
        teacher = Teacher.objects.get(user=current_user.id)
        all_classes = Class.objects.filter(classroom__teachers=teacher.id)

    user = Student.objects.filter(user__id=current_user.id)
    if user:
        student = Student.objects.get(user=current_user.id)
        all_classes = Class.objects.filter(classroom__students=student.id)
        
    context = {
        'all_classes': all_classes,
        'current_user': current_user
    }
    return render(request, 'ecweb/classes.html', context)


@login_required
def class_view(request, class_id):
    current_user = request.user
    class_obj = Class.objects.get(id=class_id)

    choices_student = []
    for student in class_obj.classroom.students.all():
        student_id = student.id
        student_name = '{}, {}'.format(
            student.user.last_name, student.user.first_name)
        choices_student.append((student_id, student_name))

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        form.fields['students'].choices = tuple(choices_student)

        if form.is_valid():
            students_to_update = [int(s)
                                  for s in form.cleaned_data['students']]
            class_obj.attendances.clear()
            class_obj.attendances.add(*students_to_update)

        return HttpResponseRedirect('/class')

    else:
        attendanced_students = [s.id for s in class_obj.attendances.all()]

        form = AttendanceForm(
            initial={'class_id': class_id, 'students': attendanced_students})
        form.fields['students'].choices = tuple(choices_student)

    context = {
        'form': form,
        'current_user': current_user,
        'class_id': class_id,
        'class_obj': class_obj
    }
    return render(request, 'ecweb/class_attendance.html', context)
