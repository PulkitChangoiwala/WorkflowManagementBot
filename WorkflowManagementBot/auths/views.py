from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import  messages
# Create your views here.


def signup_request(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + username)
            #login(request, user)
            return redirect('/auths/signin')

    return render(request, 'auths/signup.html', {'form': form})



def signin_request(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/persons/')

    context = {}
    return render(request, 'auths/login.html', context)

