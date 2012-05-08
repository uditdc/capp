# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from models import RegistrationForm,Delegates
from django.core.mail import send_mail
from django.contrib.auth.models import User
import md5


def register(request):
    template = 'register.html'

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            delegate = Delegates(username=request.POST['username'],
                                 password=md5.md5(request.POST['password']).hexdigest(),
                                 fname=request.POST['fname'],
                                 sname=request.POST['sname'],
                                 dob=request.POST['dob'],
                                 email=request.POST['email'])
            delegate.save();
            user = User.objects.create_user(request.POST['username'],
                                            request.POST['email'],
                                            request.POST['password'])
            user.save();
            #send_mail("djahfaj","aouhfpoa","udit.cp@live.com",['udit.cp@gmail.com'],fail_silently=False)
            return HttpResponse("Logged In Sucessfully")
    else :
        form = RegistrationForm()
    data = {
        'form' : form
    }
    return render_to_response(template,data,context_instance = RequestContext(request))
