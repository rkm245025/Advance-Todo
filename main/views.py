from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,TaskForm,UpdateTask,FilterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import ToDoItem
from django.db.models import Q

# Create your views here.
def about(request):
    return render(request,"main/about.html")

def filter(request):
    form=FilterForm()
    tasks=ToDoItem.objects.filter(user=request.user)
    if request.method=="POST":
        form=FilterForm(request.POST)
        if form.is_valid():
            
            if form.cleaned_data['priority']:
                tasks = tasks.filter(priority=form.cleaned_data['priority'])
            if form.cleaned_data['completed']:
                if form.cleaned_data['completed'] == 'true':
                    tasks = tasks.filter(completed=True)
                elif form.cleaned_data['completed'] == 'false':
                    tasks = tasks.filter(completed=False)
            #print(tasks)
        return render(request,"main/filter.html",{"form":form,"tasks":tasks})
    
    

    return render(request,"main/filter.html",{"form":form})

def search(request):
    if request.method=="POST":
        item=request.POST['item']
        user_task=ToDoItem.objects.filter( user=request.user , title__icontains=item)
        if user_task:
            return render(request,"main/search.html",{"items":user_task})
        else:
            messages.error(request,"task not found try to search another keywords")
            return redirect("home")
        #new_task=user_task.
        
        

def profile(request):
    user=User.objects.get(id=request.user.id)
    data=User.objects.filter(username=user)
    return render(request,"main/profile.html",{"data":data})

def home(request):
    data=None
    tasks=None
    if request.user.is_authenticated:
        form=FilterForm()
        user=User.objects.get(id=request.user.id)
        data=User.objects.filter(username=user)
        tasks=ToDoItem.objects.filter(user=user)
        #print(data.username)
    return render(request,"main/index.html",{"data":data,"tasks":tasks,"form":form})



def registration(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            messages.success(request,"Your Registraion is done succesfully!")
            login(request,user)
            return render(request,"main/home")
    return render(request,"main/registration.html",{"form":form})






def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
        #login(username=username,password=password)
            messages.success(request,"you have loged in")
            return redirect('home')
        else:
            messages.success(request,"invaid")
   
    return render(request,"main/login.html")
    

def logout_user(request):
    logout(request)
    messages.success(request,"you have been logout succesfully !")
    return redirect('home')



def task(request):
        form=TaskForm()
        if request.method=="POST":
            form=TaskForm(request.POST)
            if form.is_valid():
                my_model_instance=form.save(commit=False)
                my_model_instance.user=request.user
                my_model_instance.save()
                messages.success(request,"hey your task is added!")
                return redirect("/task")
    
    
        return render(request,"main/task.html",{"form":form})


def delete_task(request,pk):
    item=ToDoItem.objects.filter(pk=pk)
    item.delete()
    messages.success(request,"Hey your task delete succesfullly!")
    return redirect("home")


def update_task(request,pk):
    task=get_object_or_404(ToDoItem,pk=pk)
    if request.method=="POST":
        form=UpdateTask(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,"your task is update succesfully!")
            return redirect("home")
    else:
        form=UpdateTask(instance=task)
        return render(request,"main/update.html",{"form":form})
           