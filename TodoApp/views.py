from django.shortcuts import render,redirect
from django.views import View
from TodoApp.forms import UserRegisterForm,UserLoginForm,TodoForm,TodoUpdateForm
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Todos

# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request,'index.html')
    

class UserRegisterView(View):
    def get(self,request):
        form=UserRegisterForm()
        return render(request,'user_reg.html',{"form":form})
    def post(self,request):
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            fname=form.cleaned_data.get("first_name")
            lname=form.cleaned_data.get("last_name")
            uname=form.cleaned_data.get("username")
            email=form.cleaned_data.get("email")
            passw=form.cleaned_data.get("password")
            User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=passw)
            messages.success(request,"User Registered Successfully")
            return redirect('home_view')
        else:
            messages.error(request,"Invalid Data")
            return redirect('reg_view')

class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,"user_login.html",{"form":form})
    def post(self,request):
        uname=request.POST.get("username")
        passw=request.POST.get("password")
        user=authenticate(request,username=uname,password=passw)
        if user:
            login(request,user)    #saving data
            messages.success(request,"HELLO ")
            return redirect("home_view")
        else:
            messages.error(request,"invalid credentials")
            return redirect("log_view")
class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("log_view")


class TodoCreateView(View):
    def get(self,request):
        form=TodoForm()
        return render(request,"todo_create.html",{"form":form})
    def post(self,request):
        if request.user.is_authenticated:
            form=TodoForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data.get("title")
                content=form.cleaned_data.get("content")
                user=request.user
                Todos.objects.create(title=title,content=content,user=user)
                messages.success(request,"Added")
                return redirect("home_view")
            else:
                messages.error(request,"invalid data")
                return redirect('todocreate_view')
        else:
            messages.warning(request,"You must Login First")
            return redirect('log_view')

class TodoListView(View):
    def get(self,request):
        user=request.user 
        if user.is_authenticated:
            todo=Todos.objects.filter(user=request.user,status=False)
            return render(request,'todo_list.html',{"todo":todo})
        else:
            messages.warning(request,"You must login first")
            return redirect('log_view')

class TodoDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.get(id=id)
        return render(request,"todo_detail.html",{"todo":todo})

class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.get(id=id)
        todo.delete()
        return redirect ('todolist_view')
class TodoUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.get(id=id)
        form=TodoUpdateForm(instance=todo)    #instance- to get the value which already in
        return render(request,"todo_update.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.get(id=id)
        form=TodoUpdateForm(request.POST,instance=todo) 
        if form.is_valid():
            form.save()
            return redirect('todolist_view')

    

    



            






    
