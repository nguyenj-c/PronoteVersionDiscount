from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, FormView, View, ListView, DetailView
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from app.EmailBackEnd import EmailBackEnd
from app.forms.login import LoginForm


# Authentication part
def store_role_name(request, roleName):
    request.session['role'] = roleName


class LoginFormView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = EmailBackEnd.authenticate(self=self.request,username=email, password=password)
        if user is not None:
            login(self.request, user)
            if user.user_type == "1":
                store_role_name(self.request,"admin")
                return redirect(reverse('admin_home'))
            elif user.user_type == "2":
                store_role_name(self.request,"staff")
                return redirect(reverse("staff_home"))
            else:
                store_role_name(self.request,"student")
                return redirect(reverse("student_home"))

        return super().form_invalid(form)


class LogoutView(SuccessMessageMixin, TemplateView):
    def get(self, request, **kwargs):
        del request.session['role']
        logout(request)
        return redirect("/")


class HomeView(View):
    def get(self, request, **kwargs):
        if request.session['role'] == "admin":
            return render(request, "admin_home.html")
        elif request.session['role'] == "staff":
            return render(request, "staff_home.html")
        else:
            return render(request, "student_home.html")



def GetUserDetails(request):
    if request.user != None:
        return HttpResponse(
            "Utilisateur : " + request.user.email + "<br>type d'utilisateur : " + str(request.user.user_type))
    else:
        return HttpResponse("Veuillez d'abord vous connectez svp.")
