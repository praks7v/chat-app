from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm

def homepage(request):
    return render(request, 'base/homepage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'base/signup.html', {'form': form})