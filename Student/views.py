from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Student.models import Student, City, Course


# Create your views here.
@login_required
def home(request):
    return redirect('displaystudent')


@login_required
def displaystudent(request):
    return render(request, 'displaystudent.html', {'Student': Student.objects.all()})


@login_required
def addstudent(request):
    cities = City.objects.all()
    courses = Course.objects.all()
    s1 = Student.objects.all()
    return render(request, 'addstudent.html',
                  {'cities': cities, 'courses': courses})


def readstudent(request):
    s1 = Student()
    s1.fname = request.POST['tbfname']
    s1.lname = request.POST['tbfname']
    s1.mobile = request.POST['tbmobile']
    s1.email = request.POST['tbemail']
    s1.city = City.objects.get(city_name=request.POST['ddlcity'])
    s1.course = Course.objects.get(course_name=request.POST['ddlcourse'])
    s1.save()
    return redirect('displaystudent')


def update_fun(request, id):
    cities = City.objects.all()
    courses = Course.objects.all()
    s1 = Student.objects.get(id=id)
    if request.method == 'POST':
        s1.fname = request.POST['tbfname']
        s1.lname = request.POST['tbfname']
        s1.mobile = request.POST['tbmobile']
        s1.email = request.POST['tbemail']
        s1.city = City.objects.get(city_name=request.POST['ddlcity'])
        s1.course = Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.save()
        return redirect('displaystudent')
    return render(request, 'updatestudent.html',
                  {'data': s1, 'cities': cities, 'courses': courses})


def delete_fun(request, id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('displaystudent')



