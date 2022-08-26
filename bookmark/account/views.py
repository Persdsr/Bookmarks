from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm


class UserLogin(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'

    def get_success_url(self):
        return reverse_lazy('login')


def Logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

