from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView
from .models import UserInfo
from django.contrib.auth.views import logout

# Create your views here.
login_check = False
class HomePage(View):
    template = "jobportal/homepage.html"

    def get(self, request):
        return render(request, self.template, {})


class Register(View):
    template = "jobportal/registration_form.html"

    def get(self, request):
        return render(request, self.template, {})

    def post(self, request, *args, **kwargs):

        user = UserInfo.objects.filter(email= request.POST.get('email'))
        if user:
            return HttpResponse("Email ID already exists")
        else:
            if request.POST.get("firstname") and \
                    request.POST.get('lastname') and \
                    request.POST.get('email') and \
                    request.POST.get('pwd'):
                userinfo = UserInfo()
                userinfo.first_name = request.POST.get("firstname")
                userinfo.last_name = request.POST.get("lastname")
                userinfo.email = request.POST.get("email")
                userinfo.password = request.POST.get("pwd")
                userinfo.challenged = request.POST.get("Challenged")
                userinfo.save()

                if(userinfo.challenged == "Physically"):
                    return HttpResponseRedirect('psyform')
                else:
                    return HttpResponseRedirect('menform')


class UserLogin(View):
    template = "jobportal/login_form.html"

    def get(self, request):
        return render(request, self.template, {})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('email')
        password = request.POST.get('pwd')
        user = UserInfo.objects.filter(email=username, password=password)

        if user:
            global login_check
            login_check = True
            formtype = request.POST.get('challenged')
            return HttpResponseRedirect("form", formtype)
        else:
            login_check = False

        return HttpResponse("Invalid login details given")

class PsyForm(View):
    def get(self, request):
        # if login_check:
        #    return HttpResponse("Hello I am logged in")
        # else:
        #     return HttpResponse("Hello I am logged out")
        if(request.path == '/menform'):
            return render(request , "jobportal/mendisability.html")
        else:
            return render(request, "jobportal/pysdisability.html")
    def post(self, request , *args, **kwargs):
        return HttpResponse("In post")


