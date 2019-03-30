from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import View


# Create your views here.
class RegisterLoginPage(View):
    template = "jobportal/register_login_page.html"

    def get(self, request):
        return render(request, self.template, {})


class Register(View):
    template = "jobportal/registration_form.html"

    def get(self, request):
        return render(request, self.template, {})

    def post(self, request, *args, **kwargs):
        print(request.POST.get('firstname'))
        print(request.read())

        return HttpResponse("In POST REGISTER")


class Login(View):
    template = "jobportal/login_form.html"

    def get(self, request):
        return render(request, self.template, {})

    def post(self, request, *args, **kwargs):
        return HttpResponse("In POST LOGIN")

