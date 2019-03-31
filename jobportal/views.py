from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext
from django.views.generic import View
from .models import UserInfo


# Create your views here.
class HomePage(View):
    template = "jobportal/homepage.html"

    def get(self, request):
        return render(request, self.template, {})


class Register(View):
    template = "jobportal/registration_form.html"

    def get(self, request):
        return render(request, self.template, {})

    def post(self, request, *args, **kwargs):
        if request.POST.get("firstname") and \
                request.POST.get('lastname') and \
                request.POST.get('email') and \
                request.POST.get('pwd'):
            userinfo = UserInfo()
            userinfo.first_name = request.POST.get("firstname")
            userinfo.last_name = request.POST.get("lastname")
            userinfo.email = request.POST.get("email")
            userinfo.password = request.POST.get("pwd")
            userinfo.save()
        return render(request, self.template, {})


class Login(View):
    template = "jobportal/login_form.html"

    def get(self, request):
        return render(request, self.template, {})

    def post(self, request, *args, **kwargs):
        if request.POST.get('email') and request.POST.get('pwd'):
            con = RequestContext(request)
            print(con)
        return HttpResponse("S")