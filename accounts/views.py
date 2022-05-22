from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('website:homepage')
    else:
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                messages.success(request, 'Account created successfully')
                user = authenticate(email=email, password=password)
                login(request, user)
                return redirect('profile.html')

    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('website:homepage')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # email = request.POST.get('email')
            # password = request.POST.get('password')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login Successfully!")
                return redirect('accounts:profile')
            else:
                messages.success(request, "Username or password was incorrect.Try again.")
    else:
        form = LoginForm()
        return render(request, 'login.html', context={"form": form})


@login_required(login_url='accounts:login')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='accounts:login')
def user_logout(request):
    logout(request)

    return redirect('login.html')
