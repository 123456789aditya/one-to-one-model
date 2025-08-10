from django.db import models

# Create your models here.
class Aadhar(models.Model):
    aadhar=models.IntegerField(max_length=20,unique=True)
    create_date=models.DateField(max_length=20)
    created_by=models.CharField(max_length=20)
    
# class Student(models.Model):
#     stu_name=models.CharField(max_length=20)
#     stu_contact=models.IntegerField(max_length=20)
#     stu_aadharno=models.OneToOneField(Aadhar,on_delete=models.PROTECT,to_field="aadhar")