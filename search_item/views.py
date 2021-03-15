from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from .models import Information


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Information
    template_name = 'search_results.html'
