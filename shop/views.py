from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from .models import Perfume


def index(request):
    """
    Renders the homepage. Redirects unauthenticated users to the registration page.
    Displays a list of all perfumes to authenticated users.
    """
    if not request.user.is_authenticated:
        return redirect('register')
    perfumes = Perfume.objects.all()
    return render(request, 'index.html', {'perfumes': perfumes})

def register(request):
    """
    Handles user registration. If the form is valid, creates a new user, logs them in,
    and redirects them to the delivery address page.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('delivery_address')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    """
    Handles user login. Authenticates the provided username and password.
    If successful, logs in the user and redirects them to the homepage.
    Otherwise, displays an error message for invalid credentials.
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html', {"form": AuthenticationForm()})

@login_required
def perfume_detail(request, pk):
    """
    Renders a detailed view of a specific perfume. Requires the user to be logged in.
    """
    perfume = get_object_or_404(Perfume, pk=pk)
    return render(request, 'perfume_detail.html', {'perfume': perfume})

@login_required
def cart(request):
    """
    Renders the cart page. Requires the user to be logged in.
    """
    return render(request, 'cart.html')