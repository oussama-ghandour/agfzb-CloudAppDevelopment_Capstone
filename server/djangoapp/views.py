from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
from .models import CarModel
# from .restapis import related methods
from .restapis import get_dealers_from_cf,get_dealers_by_id_from_cf, get_dealer_reviews_from_cf
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)



# Create your views here.
# Create an `about` view to render a static about page
def about_view(request):
    return render(request, 'djangoapp/about.html')
# Create a `contact` view to return a static contact page
def contact_view(request):
    return render(request, 'djangoapp/contact.html')
# Create a `login_request` view to handle sign in request
def login_view(request):
    context = {}
   
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(username=username, password=password)
        if user is not None:  
            login(request, user)
            return redirect('djangoapp:index')
        else:
            # If not, return to login page again
            return render(request, 'djangoapp/login.html', context)
    else:
        return render(request, 'djangoapp/login.html', context)


# Create a `logout_request` view to handle sign out request
def logout_view(request):
    logout(request)
    return render(request,'djangoapp/index.html')

# Create a `registration_request` view to handle sign up request
def registration_view(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        user_exist = False
        try:
            # if user already exists
            User.objects.get(username=username)
            user_exist = True
        except User.DoesNotExist:
            # If not, create a new user
            logger.debug(f"{username} is a new user")
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user:
                login(request, authenticated_user)
                return redirect("djangoapp:index")  
            else:
                # if user authentication fails after registration
                context['error'] = "Failed to authenticate user."
                return render(request, 'djangoapp/login.html', context)

        context['error'] = "User already exists"
        return render(request, 'djangoapp/registration.html', context)
 

# `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        context = {}
        url = "https://oussam92ing-3000.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/dealerships/get"
        dealerships = get_dealers_from_cf(url)
        context["dealership_list"] = dealerships
       
        return render(request, 'djangoapp/index.html', context)
# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, id):
    if request.method == "GET":
        context = {}
        dealer_url = "https://oussam92ing-3000.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/dealerships/get"
        dealer = get_dealers_by_id_from_cf(dealer_url, id=id)
        context["dealer"] = dealer
        # review_url = "https://oussam92ing-5000.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/api/get_reviews"
        # reviews = get_dealer_reviews_from_cf(review_url, id=id)
        # print(reviews)
        # context["reviews"] = reviews
        return render(request, 'djangoapp/dealer_details.html', context)


# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

