from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')


def pizzas(request):
    pizzas = Pizza.objects.order_by('pizza_name')

    context = {'all_pizzas':pizzas}

    return render(request, 'MainApp/pizzas.html', context)


def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    toppings = Topping.objects.filter(pizza=p)

    context = {'pizza':p, 'toppings':toppings}

    return render(request, 'MainApp/pizza.html', context)


