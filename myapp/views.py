from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse
def home_view(request):
    return render(request, 'myapp/index.html')
def about_view(request):
    return render(request,'myapp/about.html')
def contact_view(request):
    return render(request,'myapp/contact.html')
def login_view(request):
    return render(request,"myapp/login.html")
def register_view(request):
    return render(request,"myapp/register.html")
def user_dataview(request):
    if request.method == 'POST':
        try:
            fullname = request.POST['fname']
            email = request.POST['email']
            password = request.POST['password']
            contact = request.POST['contact']
            dob = request.POST['dob']
            gender = request.POST['gender']
        except KeyError:
            message = "Invalid form data. Please fill all fields."
            return render(request, "myapp/register.html", {'msg': message})
        
        user = Customer.objects.filter(Email=email)

        if user:
            message = "User already exists"
            return render(request, "myapp/register.html", {'msg': message})
        else:
            message = "Successfully registered, please login"
            new_user = Customer.objects.create(Fullname=fullname, Email=email, Password=password, Contact=contact, Dob=dob, Gender=gender)
            return render(request, "myapp/login.html", {'msg': message})
    else:
        return HttpResponse("Invalid Request Method")

def user_loginview(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = Customer.objects.get(Email=email)
        except Customer.DoesNotExist:
            message = "User does not exist. Please register."
            return render(request, "myapp/register.html", {'msg': message})
        if user.Password==password:
            request.session['Fullname']=user.Fullname
            request.session['Email']=user.Email
            request.session['Dob']=user.Dob
            request.session['Gender']=user.Gender
            request.session['Contact']=user.Contact
            return render(request,"myapp/user_home.html")
        else:
            message="Password does not match"
            return render(request,"myapp/login.html",{'msg':message})
def user_logoutview(request):
    # remove session data
    request.session.flush()
    # redirect to login page
    return redirect('home')
def after_loginhomeview(request):
    return render(request,"myapp/user_home.html")
def offer_views(request):
    return render(request,"myapp/offer.html")
def earn_money_views(request):
    return render(request,"myapp/earn_money.html")
def profile_views(request):
    return render(request,"myapp/profile.html")


