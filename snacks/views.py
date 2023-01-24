from django.views.generic import DetailView, ListView, TemplateView
from .models import Snack

class HomePageView(TemplateView):
    template_name = 'home.html'


class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack


class SnackDetailView(ListView):
    template_name = 'snack_detail.html'
    model = Snack

