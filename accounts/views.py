from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from .forms import UserRegistrationForm


class RegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/registration.html'
# class RegistrationView(View):
#     template_name = 'registration/registration.html'

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print("test")
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались  ')
            return redirect
        return render(request, self.template_name, {'form': form})