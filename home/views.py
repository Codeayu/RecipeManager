from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings


# Create your views here.

def home(request):
    return render(request, 'index.html')

def login_us(request):
    if request.method == 'POST':
        usernm = request.POST['username']
        passwd = request.POST['password']

        # Check if the user exists
        try:
            user = User.objects.get(username=usernm)
        except User.DoesNotExist:
            messages.info(request, 'User is not available')
            return redirect('/register/')

        # Authenticate the user
        user = authenticate(username=usernm, password=passwd)
        if user is None:
            messages.error(request, 'Incorrect password')
            return redirect('/login_us/')
        else:
            login(request, user)  # Log the user in
            return redirect('/show_recepies/')  # Redirect to homepage or another page after login

    return render(request, 'login.html')

def register(request):
    if request.method =='POST':
        firstnm = request.POST['fname']
        lastnm = request.POST['lname']
        usernm = request.POST['username']
        passwd = request.POST['password']
        
        user = User.objects.filter(username = usernm)
        if user.exists():
            messages.info(request, 'username already taken ')
            return redirect("/register/")

        user = User.objects.create(
            first_name = firstnm,
            last_name = lastnm,
            username = usernm
        )
        user.set_password(passwd)
        user.save()
        messages.info(request, 'username created succesfully')
        return redirect('/login_us/')
    return render(request, 'register.html')

@login_required
def show_recepies(request):
    recipes = Recipe.objects.all()
    return render(request, 'show_recepies.html',context={"recipes":recipes})

def logout_us(request):
    logout(request)
    return redirect('home')


@login_required
def add_recipe(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)

        recipe_name = request.POST.get('recipe_name')  # Use .get() for safety
        description = request.POST.get('description') 
        recipe_img = request.FILES.get('recipe_img') 
        food_type = request.POST.get('food_type') 
        steps = request.POST.get('steps')

        recipe = Recipe.objects.create(

        user = request.user,
        recipe_name=recipe_name,
        description=description,
        recipe_img=recipe_img,
        food_type=food_type,
        steps=steps
       )

        recipe.save()
        return redirect('/show_recepies/')
    return render(request, 'add_recipe.html')

@login_required
def edit(request,rid):
    recipes = get_object_or_404(Recipe, id=rid)
    
    
    if request.method == 'POST':
        recipes.recipe_name = request.POST.get('recipe_name')
        recipes.description = request.POST.get('description')
        recipes.food_type = request.POST.get('food_type')
        recipes.steps = request.POST.get('steps')

        if 'recipe_img' in request.FILES:  # Handle image upload
            recipes.recipe_img = request.FILES['recipe_img']

                     
        recipes.save()
        return redirect('show_recepies')

    return render(request, 'edit.html', {'recipe': recipes})


@login_required
def delete(request,rid):
    recipe = get_object_or_404(Recipe, id=rid)

    if request.method == 'POST':
        recipe.delete()


        return redirect('show_recepies')
    return render(request, 'delete.html')

def contact(request):
    return render(request, 'contact.html', {'MEDIA_URL': settings.MEDIA_URL})