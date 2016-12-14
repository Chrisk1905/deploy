from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        'all_courses': Course.objects.all(),
    }
    return render(request, 'courses_table/index.html', context)

def add_course(request):
    Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def destory(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id),
    }
    return render(request, 'courses_table/show.html', context)

def delete(request, course_id):
    Course.objects.get(id = course_id).delete()
    return redirect('/')
