from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import SignUpFrom
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.

class SignUpView(View):
    template_name = 'accounts/sign_up.html'

    def get(self, request):
        form = SignUpFrom()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            raw_pasword = form.cleaned_data.get('password1')
            user = authenticate(username=user_name, password=raw_pasword)
            login(request, user)
            messages.success(request, "Sign Up is completed successfully and Login successfully")
            return redirect('core:home')
        return render(request, self.template_name, {'form': form})

class LoginView(View):
    template_name = 'accounts/login.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:home')
        else:
            return render(request, self.template_name)
        
    def post(self, request):
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        user = authenticate (username = username, password = password)
        if user is not None:
            login (request, user)
            messages.success(request, "You are logged in successfully")
            return redirect('core:home')
        return render(request, self.template_name)


class LogOutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You are Logged Out successfully")
        return redirect("accounts:login")
        


