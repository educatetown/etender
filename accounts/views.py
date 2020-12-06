from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import UserForm, ProfileForm
# Create your views here.


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
            return redirect('tender:all')

        else:
            print(user_form.errors, profile_form.errors)


    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'registration.html', {'user_form':user_form,
                                                          'profile_form':profile_form,
                                                          'registered':registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('tender:all'))

            else:
                messages.error(request, "Invalid username or password.")
                return HttpResponse("Account not active")

        else:
            messages.error(request, "Invalid username or password.")
            return redirect('tender:all')

    else:
        return render(request, 'accounts/login.html')
