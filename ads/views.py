#from django.shortcuts import render

# Create your views here.
from django.views import generic
from . import models

class AdsIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 10