from django.shortcuts import render
from .models import Aadhar,Student
# Create your views here.


def student(request):
    data=Student.objects.all()
    print(data.values())
    
def aadhar(request):
    all_data=Aadhar.objects.all()
    print(aadhar.values())