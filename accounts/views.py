from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm

User = get_user_model()


def register_view(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        confirm_password = register_form.cleaned_data.get('confirm_password')

        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None

        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['registration_error'] = 1

    return render(request, 'register.html', {"register_form": register_form})


def login_view(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user != None:
            # request.user == user ---> user is valid and active -> is_active
            login(request, user)
            return redirect("/")
        else:
            # attempt = request.session.get('attempt') or 0
            # request.session['attempt'] = attempt + 1
            request.session['invalid_user'] = 1  # 1 == True
    return render(request, 'login.html', {"login_form": login_form})


def logout_view(request):
    logout(request)
    return redirect('/login')
