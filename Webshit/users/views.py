from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #Change UserCreationForm with UserRegisterForm
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, you are now be able to log in')
            return redirect('login')
        elif not form.is_valid():
            messages.success(request, f'Account failed to create !!!')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', { 'form': form })

@login_required
def profile(request):
    return render(request, 'users/profile.html')