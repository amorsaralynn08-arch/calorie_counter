from django.shortcuts import *
from .models import *

# Create your views here.
def home(request):
    foods = Food.objects.all()
    total_calories = sum(food.calories for food in foods)

    context = {
        "foods": foods,
        "total_calories": total_calories,
    }

    return render(request, "home.html", context)