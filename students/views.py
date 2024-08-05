
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404

from .forms import StudentForm, GradeForm
from .models import Student, Grade


def view_home(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'students/index.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view_home')
        else:
            messages.success(request, ("Invalid username or password. Please try again!"))
            return redirect('/')
    else:
        return render(request, 'login.html', {})


def log_out(request):
    logout(request)
    messages.success(request, ("You logged out successfully!"))
    return redirect('/')





def view_pythonintermediate(request):
    grade_values = Grade.objects.filter(subject_id=2)
    context = {
        'grade_values': grade_values,
    }

    return render(request, 'students/pythonIntermediate.html',context)


def view_sql(request):
    grade_values = Grade.objects.filter(subject_id=3)
    context = {
        'grade_values': grade_values,
    }
    return render(request, 'students/sqldatabase.html',context)


def view_frontend(request):
    grade_values = Grade.objects.filter(subject_id=4)
    context = {
        'grade_values': grade_values,
    }
    return render(request, 'students/frontend.html',context)


def view_backend(request):
    grade_values = Grade.objects.filter(subject_id=5)
    context = {
        'grade_values': grade_values,
    }
    return render(request, 'students/backend.html',context)


def view_schedule(request):
    return render(request, 'students/schedule.html')


# C.R.U.D functions:

@permission_required('students.add_student')
def create_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_home')
    else:
        form = StudentForm

    context = {'form': form}
    return render(request, 'students/create_view.html', context)


@permission_required('students.change_student')
def update_view(request, id):
    obj = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('view_home')
    else:
        form = StudentForm(instance=obj)

    context = {'form': form}
    return render(request, 'students/update_view.html', context)


@permission_required("students.give_medal")
def delete_view(request, id):
    obj = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('view_home')
    return render(request,"students/delete_view.html")


def info_view(request, id):
    student = get_object_or_404(Student, id=id)
    grades = Grade.objects.filter(student=student)

    if grades.exists():
        GPA = grades.aggregate(Avg('grade'))['grade__avg']
    else:
        GPA = None

    context = {
        'student': student,
        'grades': grades,
        'GPA': GPA
    }
    return render(request, 'students/info_view.html', context)


# --------------------------------------
def view_pythonbasic(request):
    grade_values = Grade.objects.filter(subject_id=1)
    context = {
        'grade_values': grade_values,
    }
    return render(request, 'students/pythonBasic.html', context)


def add_grades(request):
    if request.method == 'POST':
        form = GradeForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            if subject.name == 'Backend Technologies':
                form.save()
                return redirect('view_backend')

            elif subject.name == 'Python the basic':
                form.save()
                return redirect('view_pythonbasic')

            elif subject.name == 'Python intermediate':
                form.save()
                return redirect('view_pythonintermediate')

            elif subject.name == 'SQL Databases':
                form.save()
                return redirect('view_sql')

            elif subject.name == 'HTML, CSS and Javascript':
                form.save()
                return redirect('view_frontend')

    else:
        form = GradeForm

    context = {'form': form}
    return render(request, 'students/grade.html', context)


def delete_row(request, id):
    obj = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('view_pythonbasic')
    return render(request,"students/delete_view.html")

def gpa_calc():
    all_grades = Grade.objects.filter('grade')
