# Create your views here.
from django.contrib.auth import authenticate,login
from django.shortcuts import render_to_response
def doLogin(request):
    msg = "Please Log in ..."
    
    if request.POST:
        user = authenticate(username = request.POST['username'],password = request.POST['password'])
        if user is not None : 
            if user.is_active :
                login(request,user)
                msg = "Logged in Sucessfully"
            else:
                msg = "Account is not active"
        else:
            msg = "Username and/or Password is wrong"
    
        
    