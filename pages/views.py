from django.shortcuts import render
from django.views.generic import View, FormView, CreateView
from newsletter.forms import JoinForm
# Create your views here. JoinFor


class HomeView(CreateView):
    template_name = "pages/home.html"
    form_class = JoinForm
    success_url = ('/')
#class HomeView(View):
 #   def get(self, request, *args, **kwrgs):
  #      return render(request, "pages/home.html", {})