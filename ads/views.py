from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from django.views import generic
from . import models
from .forms import AdForm

class AdsIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 10

class AdsList(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "list.html"
    paginate_by = 50

def ad_details(request, slug):
    queryset = models.Entry.objects.published()
    ad = get_object_or_404(queryset, slug=slug)
    return render(request, 'ad-detail.html', {'ad':ad})

def ad_new(request):
    form = AdForm(request.POST, request.FILES)

    if form.is_valid():
        post = form.save(commit=False)
        post.save()
    
    return render(request, 'ad_new.html', {'form': form})
