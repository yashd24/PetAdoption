from django.shortcuts import render, redirect
from .forms import MyForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Animal


@login_required(login_url='login')
def home(request):
    ele = Animal.objects.all()
    return render(request, 'Adoption/home.html', {'ele': ele})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        ele = Animal.objects.all()
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return render(request, 'Adoption/adminhome.html', {'ele': ele})
            else:
                return render(request, 'Adoption/loggedin.html', {'ele': ele})
        else:
            error = 'Incorrect Credentials'
            messages.error(request, error)
            return redirect('login')
    return render(request, 'Adoption/login.html')


def SignUp(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'Adoption/signup.html', {'form': form})


@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        # Pass request.FILES for file uploads
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            species = form.cleaned_data['species']
            breed = form.cleaned_data['breed']
            color = form.cleaned_data['color']
            description = form.cleaned_data['description']
            location = form.cleaned_data['location']
            contact = form.cleaned_data['contact']
            img = form.cleaned_data['img']
            availabilitystatus = bool(
                request.POST.get('supportCheckbox', False))
            uploadedby = request.user
            animal = Animal(species=species, breed=breed, color=color,
                            description=description, location=location,
                            contact=contact, img=img, availabilitystatus=availabilitystatus, uploadedby=uploadedby)
            animal.save()

            return redirect('home')

    else:
        form = MyForm()

    return render(request, 'Adoption/add.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def delete(request, animalid):
    animal = Animal.objects.get(animalid=animalid)
    if request.method == "POST":
        animal.delete()
        print(animal)
        return redirect('home')
    return render(request, "Adoption/delete.html", {'obj': animal})


def update(request, animalid):
    animal = Animal.objects.get(animalid=animalid)
    form = MyForm(request.POST, request.FILES, instance=animal)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'Adoption/add.html', {'form': form})


def detail(request, animalid):
    animal = Animal.objects.get(animalid=animalid)
    return render(request, 'Adoption/detail.html', {'animal': animal})
