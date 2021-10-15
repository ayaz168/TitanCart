from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import re 
# Create your views here.
def check(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex,email)):  
        return True
    return False
def password_check(password):
    """
    My Function For SE Project Ecommerce
    Ayaz Afzal
        Minimum 8 Character
        1 Min Numeric Char
        1 Min Symbol
        1 UpperCase Char
        1 Lowercase Char
    """
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"\W", password) is None
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )
    if  password_ok:
        return True
    else:
        return False
def password_checkM(password):
    """
    My Function For SE Project Ecommerce
    Ayaz Afzal
        Minimum 8 Character
        1 Min Numeric Char
        1 Min Symbol
        1 UpperCase Char
        1 Lowercase Char
    """
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"\W", password) is None
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )
    if  password_ok:
        Message="Password Correct"
    else:
        Message="Your Password is Invalid as : "
        if length_error:
            Message+='Low Lenghth'
        if digit_error:
            Message+=', No Numeric Character in Password'
        if uppercase_error:
            Message+=', No UpperCase Character '
        if lowercase_error:
            Message+=', No LowerCase Error '
        if symbol_error:
            Message+=', No Symbol'
    return Message
def logoutH(request):
    auth.logout(request)
    messages.info(request,"Log Out Succesful.")
    return redirect('/')
def loginH(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"Logged In.")
            return redirect('/')
        else:
            messages.info(request,'Invalid Credientials for Login.')
            return redirect('login')
    else:
        return render(request,'login.html')
def nameCheck(first_name,last_name):
    sFName_error=not(re.search(r'\d+', first_name) is None)
    sLName_error=not(re.search(r'\d+', last_name) is None)
    if   sFName_error or sLName_error :
        return False #returns false if invalid
    return True
def getNameError(first_name,last_name):
    sFName_error=not(re.search(r'\d+', first_name) is None)
    sLName_error=not(re.search(r'\d+', last_name) is None)
    Message="Invalid Entry : "
    if sFName_error:
        Message+=', Wrong First Name. No digits allowed '
    if sLName_error:
        Message+=', Wrong Last Name. No digits allowed  '
    return Message 
def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if nameCheck(first_name,last_name):
            if password1==password2: # Password Should be same for SignUp
                if User.objects.filter(username=username).exists(): # Username is already taken
                    messages.info(request,'UserName Taken!')
                    return redirect('signup')
                elif User.objects.filter(email=email).exists():# Emmail is already taken
                    messages.info(request,'Email Taken!')
                    return redirect('signup')
                else:
                    if password_check(password1):
                        if check(email):
                            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                            user.save()
                            messages.info(request,"SignUp Success.")
                            return redirect('/')#success
                        else:
                            messages.info(request,'Please Enter A Valid Email address')
                            return redirect('signup')
                    else:
                        Msg=password_checkM(password1)
                        messages.info(request,Msg)
                        return redirect('signup')
            else:
                messages.info(request,'Password Not Matching')
                return redirect('signup')
        else:
            messages.info(request,getNameError(first_name,last_name))
            return redirect('signup')
    else:
        return render(request,'login.html')
def contactus(request): 
    return render(request,'contact-us.html')