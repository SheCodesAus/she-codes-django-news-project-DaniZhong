import email
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db import models

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

from django.shortcuts import render


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'


class ViewAccountView(generic.DetailView):
    model = CustomUser
    template_name = 'users/viewAccount.html'
    context_object_name = 'user'