from django.shortcuts import render,redirect
from blog.forms import SignupForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from blog.models import Post,Contact
# Create your views here.
# home
def home(request):
    current_user=request.user
    post=Post.objects.all().order_by('-timestamp')
    return render(request,"blog/home.html",{"posts":post})
# about
def about(request):
    return render(request,"blog/about.html")

# contact
def contact(request):
    if request.method=="POST":
        name1=request.POST.get("name")
        email1=request.POST.get("email")
        address1=request.POST.get("address")
        message1=request.POST.get("message")
        contact=Contact(name=name1,email=email1,address=address1,message=message1)
        contact.save()
        return redirect("/")  
    return render(request,"blog/contact.html")

# dashboard
def dashboard(request):
    if request.user.is_authenticated:
        current_user=request.user
        full_name=current_user.get_full_name()
        post=Post.objects.filter(author=current_user)
        return render(request,"blog/dashboard.html",{"posts":post,"full_name":full_name})
    else:
        return redirect("/login/")

# signin
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=SignupForm(request.POST)
            if form.is_valid():
                messages.success(request,"Welcome! Be the Author of your own Story.")
                form.save()
        else:
            form=SignupForm()
    else:
        return redirect("/dashboard/")
    return render(request,"blog/signup.html",context={"form":form})

# login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data["username"]
                upass=form.cleaned_data["password"]
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in successfully..!")
                    return redirect("/dashboard/")
        else:
            form=LoginForm()
    else:
        return redirect('/dashboard/')
    return render(request,"blog/login.html",{'form':form})

# logout
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")
    else:
        return redirect("/login/")
# Add a post 
def add_post(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=PostForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user.username
                instance.save()
                return redirect("/dashboard/")
        else:
            form=PostForm()
        return render(request,"blog/addpost.html",{"forms":form})
    else:
        return redirect('/login/')
    
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":           
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                return redirect("/dashboard/")
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request,"blog/updatepost.html",{"forms":form})
    else:
        return redirect('/login/')
    
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            pi.delete()
        return redirect("/dashboard/")
    else:
        return redirect("/login/")