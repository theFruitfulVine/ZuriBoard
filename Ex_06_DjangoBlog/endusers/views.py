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
    eu_form = UserUpdateForm()
    pr_form = ProfileUpdateForm()

    context = {
        'eu_form' : eu_form,
        'pr_form' : pr_form
    }
    return render(request, 'endusers/profile.html')
