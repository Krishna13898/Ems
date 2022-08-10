

from re import I
from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . models import * 
from . forms import * 

# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,' Account was created for ' + username)

            return redirect('login')

    context = {'form':form}
    return render(request,'register.html',context)




def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username OR Password is incorrect')

    context = {}
    return render(request,'login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def home(request):
    manager = request.user.manager.id

    
    emp = request.user.manager.employee_set.all()
    context = {'emp':emp}
    return render(request,'home.html',context)



@login_required(login_url='login')
def addEmployee(request):
    manager = request.user.manager
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.manager_id = manager

            employee.save()
            return redirect('home')


    context = {'form':form}
    return render(request,'employee_form.html',context)




@login_required(login_url='login')
def updateEmployee(request,pk):
    manager = request.user.manager
    emp = manager.employee_set.get(id=pk)
    
    form = EmployeeForm(instance=emp)

    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            emp = form.save()
            return redirect('home')


    context = {'form':form,'emp':emp}
    return render(request,'employee_form.html',context)




@login_required(login_url='login')
def deleteEmployee(request,pk):
    manager = request.user.manager
    
    emp = manager.employee_set.get(id=pk)

    if request.method == 'POST':
        emp.delete()
        return redirect('home')

    context = {'object':emp}
    return render(request,"delete_template.html",context)