from django.shortcuts import render 
from courses.models import Course 
from django.shortcuts import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator


def Cse(request,data=None):
    if data == None:
        cse = Course.objects.filter(category='cse')
    elif data == 'Programming' or data == 'DBMS' or data == 'Math':
        cse = Course.objects.filter(category='cse').filter(subCategory=data)
    elif data == 'below':
        cse = Course.objects.filter(category='cse').filter(discount__lt=20)
    elif data == 'above':
        cse = Course.objects.filter(category='cse').filter(discount__gt=20)
    return render(request, 'courses/cse.html',{'cse':cse})

def Bba(request,data=None):
    if data == None:
        bba = Course.objects.filter(category='bba')
    elif data == 'Management' or data == 'Accounting' or data == 'Math':
        bba = Course.objects.filter(category='bba').filter(subCategory=data)
    elif data == 'below':
        bba = Course.objects.filter(category='bba').filter(discount__lt=20)
    elif data == 'above':
        bba = Course.objects.filter(category='bba').filter(discount__gt=20)
    return render(request, 'courses/bba.html',{'bba':bba})