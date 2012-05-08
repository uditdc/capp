# Create your views here.
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from django.http import HttpResponse
from models import LoginForm
#def doLogin(request):
#    msg = "Please Log in ..."
#    if request.POST:
#        user = authenticate(username = request.POST['username'],password = request.POST['password'])
#        if user is not None : 
#            if user.is_active :
#                login(request,user)
#                msg = "Logged in Sucessfully"
#            else:
#                msg = "Account is not active"
#        else:
#            msg = "Username and/or Password is wrong"
#    return HttpResponse(msg)
        
def doLogin(request):
    template = 'login.html'
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = request.POST['username'],password = request.POST['password'])
            if user is not None : 
                if user.is_active :
                    login(request,user)
                    msg = "Logged in Sucessfully"
                else:
                    msg = "Account is not active"
            else:
                msg = "Username and/or Password is wrong"
            return render_to_response(template,{'msg':msg},context_instance = RequestContext(request))
    else :
        form = LoginForm()
    data = {
        'form' : form
    }
    return render_to_response(template,data,context_instance = RequestContext(request))


def doLogout(request):
    logout(request)
    return render(request,'index.html',{},context_instance = RequestContext(request))