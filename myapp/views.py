from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
import json
import random
# Create your views here.


def index(request):
	return redirect('graph')


def graph(request):
	random_value = random.randint(1,11)*0.1
	return render(request,"myapp/graph.html",{'random_value':mark_safe(json.dumps(random_value))})

