from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from . import forms
from django.contrib.auth.decorators import login_required


# Create your views here.
def account(request):
    return render(request, 'account/dashboard.html')


def user_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password']
                                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'account/dashboard.html', {'user': user})
                else:
                    return HttpResponse('Disable account')

            else:
                return HttpResponse('Invalid login')

    else:
        form = forms.LoginForm()
        return render(request, 'account/registration/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = forms.UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
        return render(request,
                      'account/registration/register_done.html',
                      {'new_user': new_user})

    else:
        user_form = forms.UserRegistrationForm()
        return render(request,
                      'account/registration/register.html',
                      {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = forms.UserEditForm(instance=request.user,
                                       data=request.POST)
        profile_form = forms.ProfileEditForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(request, 'Error updating your profile.')

    else:
        user_form = forms.UserEditForm(instance=request.user)
        profile_form = forms.ProfileEditForm(
            instance=request.user)

    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


def user_profile(request, pk):
    user = User.objects.get(pk=pk)
    context = {
       "user": user
    }


    return render(request, 'account/user_profile.html', context)