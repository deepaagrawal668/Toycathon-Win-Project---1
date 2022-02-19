from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from quizoApp.models import Profile

def login(request):
    return render(request, 'login.html')

def login_attempt(request):
    if request.method=='POST':
        # print(request.POST)
        name = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username= name, password = password)


        if user is not None:
            auth.login(request, user)
            return redirect('/success/')
        else:
            return HttpResponse("Invalid credentials")
    return HttpResponse('bad request')

def register_attempt(request):
    if request.method=='POST': 
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        mobile_number = request.POST['phn_no']
        dob = request.POST['dob']
        gender = request.POST['gender']
        role = request.POST['role']
        user_name = request.POST['username']
        password = request.POST['pass']
        confirmpassword = request.POST['confpass']
        if password == confirmpassword:
            if User.objects.filter(username = user_name).exists():
                return HttpResponse('Username taken')
            elif User.objects.filter(email = email).exists():
                return HttpResponse("Email taken")
            else:
                isStudent = False
                isCreator = False
                isApprover = False
                user_obj = User.objects.create_user(username = user_name, password = password, email = email, first_name = first_name, last_name = last_name)
                if(role == 'student'):
                    isStudent = True
                if(role == 'creator'):
                    isStudent = True
                    isCreator = True
                if(role == "approver"):
                    isStudent = True
                    isCreator = True
                    isApprover = True
                profile_obj = Profile.objects.create(user = user_obj, id = user_name,dob = dob, gender = gender, mobile_number = mobile_number, isStudent = isStudent, isCreator = isCreator, isApprover = isApprover )
                user_obj.save();
                profile_obj.save();
                return redirect('/success/')
        else:
            return HttpResponse('Password is not matching')
    return HttpResponse('bad request')

def Registration(request):
    return render(request, 'register.html')

def success(request):
    return render(request, 'thank_you.html')

