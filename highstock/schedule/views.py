from django.shortcuts import render
from django.http import JsonResponse
import random
import time

from .models import Schedule


def index(request):
    timing = time.time()
    while True:
        if time.time() - timing > 1.0:
            n = random.randint(1, 500)
            data = {"graph": n, "graph1": 2, "graph2": 1, "graph3": 3}
            return render(request, "schedule/index.html", context=data)


def get_random_data(request):
    n = random.randint(1, 500)

    # Подвязка к БД
    obj, created = Schedule.objects.get_or_create(values=n)
    if created:
        obj.save()

    data = {"graph": n, "graph1": 2, "graph2": 1, "graph3": 2}
    return JsonResponse(data=data)

