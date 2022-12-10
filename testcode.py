import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import *


toppings = Pizza.objects.all()

print(toppings)

for t in toppings:
    print(t)


toppings = Topping.objects.filter(pizza=t)

for t in toppings:
    print(t.topping_name)