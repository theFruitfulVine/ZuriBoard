from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserSignupForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}'s fruitfulblog account created!")
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'endusers/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        eu_form = UserUpdateForm(request.POST, instance=request.user)
        pu_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if eu_form.is_valid() and pu_form.is_valid():
            eu_form.save()
            pu_form.save()
            messages.success(request, f'Your Profile info has been updated!')
            return redirect('profile')
    else:
        eu_form = UserUpdateForm(instance=request.user)
        pu_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'eu_form' : eu_form,
        'pu_form' : pu_form
    }
    return render(request, 'endusers/profile.html', context)
