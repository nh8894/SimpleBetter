from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login 
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('boards:index')
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('boards:index')


class RegisterView(CreateView):
    form_class = RegisterForm

    template_name = 'accounts/login.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('boards:index')
            #
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_activate:
                        login(request, user)
                        return redirect('boards:index')

        return render(request, self.template_name, {'form': form})
