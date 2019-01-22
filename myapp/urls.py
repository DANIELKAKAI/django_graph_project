from django.urls import re_path,path
from myapp.views import index,graph

urlpatterns = [
	re_path(r'^$',index,name="index"),
	path('graph/',graph,name="graph")
]