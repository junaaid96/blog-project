from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForm()
#     return render(request, 'add_author.html', {'author_form': author_form})

def registration(request):
    if request.method == 'POST':
        registration_form = forms.RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('registration')
    else:
        registration_form = forms.RegistrationForm()
    return render(request, 'registration.html', {'form': registration_form, 'type': 'Registration'})


def user_login(request):
    if request.method == 'POST':
        # here request is the request object that is passed to the view. request.POST is a dictionary that contains all the data that is submitted via the form. We pass this data to our form and create an instance of it.
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data.get('username')
            user_password = login_form.cleaned_data.get('password')
            user = authenticate(username=user_name, password=user_password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password!')
                return redirect('registration')
    else:
        login_form = AuthenticationForm()
    return render(request, 'registration.html', {'form': login_form, 'type': 'Login'})


@login_required
def profile(request):
    if request.method == 'POST':
        # request.POST is a dictionary that contains all the data that is submitted via the form. We pass this data to our form and create an instance of it. We also pass the instance of the user that is currently logged in. So it displays the current data of the user in the form.
        profile_form = forms.ChangeUserDataForm(
            request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')

    else:
        profile_form = forms.ChangeUserDataForm(instance=request.user)
    return render(request, 'profile.html', {'form': profile_form})


def user_logout(request):
    logout(request)
    return redirect('home')
