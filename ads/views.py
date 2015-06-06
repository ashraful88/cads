from django.shortcuts import render

# Create your views here.
from django.views import generic
from . import models
from .forms import AdForm

class AdsIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 10

def ad_new(request):
    form = AdForm(request.POST, request.FILES)

    if form.is_valid():
        post = form.save(commit=False)
        post.save()
    
    return render(request, 'ad_new.html', {'form': form})