from django.shortcuts import render, redirect
# imports the user creation form for the register view
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegForm, UserUpForm, ProfileUpForm

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, You can now login')
            return redirect('login')

    else:
        form = UserRegForm()
    return render(request, 'Users/register.html', {'form': form})

@login_required
def Profile(request):
    if request.method == 'POST':
        user_form = UserUpForm(request.POST, instance=request.user)
        profile_form = ProfileUpForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('UserProfile')
    else:
        user_form = UserUpForm(instance=request.user)
        profile_form = ProfileUpForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'Users/UserProfile.html', context)

