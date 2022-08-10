
from django.db import models

from django.contrib.auth.models import User
# Create your models here.




class Manager(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=200,blank=True,null=True)
    first_name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    dob = models.DateField(auto_now=False, auto_now_add=False,null=True)
    company_name= models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return str(self.first_name +" "+ self.last_name)

class Employee(models.Model):
    manager_id = models.ForeignKey(Manager,on_delete=models.CASCADE,null=True,blank=True)
    empId = models.CharField(max_length=100,blank=True,null=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    dob = models.DateField(auto_now=False, auto_now_add=False,null=True)
    mobile = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.first_name +" "+ self.last_name +" "+ self.empId)
