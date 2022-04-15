from django.shortcuts import render
import random
import time


def index(request):
    timing = time.time()
    while True:
        if time.time() - timing > 1.0:
            n = random.randint(1, 500)
            data = {"graph": n, "graph1": 2, "graph2": 1, "graph3": 2}
            return render(request, "schedule/index.html", context=data)