from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login  # ⬅ alias Django's login

def login_view(request):  # ⬅ rename your login view
    return render(request, 'login.html')

# Create your views here.

def index(request):
    books=Book.objects.all()
    return render(request,'index.html',{'books':books})


def product_details(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "products_details.html", {'book': book})


def login(request):
    return render(request,'login.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        confpwd = request.POST.get('confirmPassword')

        if pwd != confpwd:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():  # ⬅ FIXED `.exists()`
            messages.error(request, "Username already exists")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=pwd)
        user.save()

        auth_login(request, user)  # ⬅ use Django's login
        messages.success(request, "Registration Successful")
        return redirect('index')  # ⬅ use named URL pattern

    return render(request, "register.html")
