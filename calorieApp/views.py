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

def add_food(request):
    if request.method == "POST":
        food_name = request.POST.get("food_name")
        calories = request.POST.get("calories")

        Food.objects.create(
            food_name=food_name,
            calories=calories
        )

        return redirect("home")

    return render(request, "add_food.html")

def delete_food(request, id):
    food = get_object_or_404(Food, id=id)
    food.delete()

    return redirect("home")

def reset_calories(request):
    Food.objects.all().delete()

    return redirect("home")