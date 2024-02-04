from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from dotenv import load_dotenv
# from .models import related models
from .models import CarModel
# from .restapis import related methods
from .restapis import get_dealers_from_cf,get_dealers_by_id_from_cf, get_dealer_reviews_from_cf, post_request
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
import os

load_dotenv()

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
        url = os.getenv('dealer_key')
        dealerships = get_dealers_from_cf(url)
        context["dealership_list"] = dealerships
       
        return render(request, 'djangoapp/index.html', context)
# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, id):
    if request.method == "GET":
        context = {}
        dealer_url = os.getenv('dealer_key')
        dealer = get_dealers_by_id_from_cf(dealer_url, id=id)
        context["dealer"] = dealer
        review_url = os.getenv('review_key')
        reviews = get_dealer_reviews_from_cf(review_url, id=id)
        print(reviews)
        context["reviews"] = reviews
        return render(request, 'djangoapp/dealer_details.html', context)
# Create a `add_review` view to submit a review
def add_review(request, id):
    context = {}
    url = os.getenv('dealer_key')
    dealer = get_dealers_by_id_from_cf(url, id=id)
    context["dealer"] = dealer
    if request.method == "GET":
        cars = CarModel.objects.all()
        print(cars)
        context["cars"] = cars

        return render(request, 'djangoapp/add_review.html', context)
    elif request.method == "POST":
        print(request.POST)
        if request.user.is_authenticated:
            username = request.user.username
            print(request.POST)
            payload = dict()
            car_id = request.POST.get("car")
            print(car_id)
            car = CarModel.objects.get(pk=car_id)
            payload["time"] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            payload["name"] = username
            payload["dealership"] = id
            payload["id"] = id
            payload["review"] = request.POST["content"]
            payload["purchase"] = False
            if "purchasecheck" in request.POST:
                if request.POST["purchasecheck"] == 'on':
                    payload["purchase"] = True
            payload["purchase_date"] = request.POST.get("purchase_date")
            payload["car_make"] = car.car_make.name
            payload["car_model"] = car.name
            payload["car_year"] = int(car.year.strftime("%Y"))

            new_payload = {}
            new_payload["review"] = payload
            post_url  = os.getenv('review_key')
            review = {
                "id" : id,
                "time" : datetime.utcnow().isoformat(),
                "name" : request.user.username,
                "dealership" : id,
                "review" : request.POST["content"],
                "purchase" : True,
                "purchase_date" : request.POST.get("purchase_date"),
                "car_make" : car.car_make.name,
                "car_model" : car.name,
                "car_year" : int(car.year.strftime("%Y")),
            }
            review=json.dumps(review,default=str)
            new_payload1 = {}
            new_payload1["review"] = review
            print("\nREVIEW:",review)
            post_request(post_url, review, id=id)
            print("successfully posted")
        return redirect("djangoapp:dealers_details", id=id)

            






