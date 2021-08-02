
from django.views.generic import ListView
from django.shortcuts import render
from courses.models import Course , UserCourse

class HomePageView(ListView):
    template_name = "courses/home.html"
    queryset = Course.objects.filter(active=True)
    context_object_name = 'courses'

def search(request):
    query = request.GET['query']
    result = Course.objects.filter(name__icontains=query)
    return render(request,'courses/search.html',{'user_courses':result})

def course(request):
    query = Course.objects.all()
    return render(request,'courses/course.html',{'courses':query})
