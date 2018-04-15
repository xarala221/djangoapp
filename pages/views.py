from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View, FormView, CreateView
from newsletter.forms import JoinForm
from pages.models import Page
# Create your views here. JoinFor


class HomeView(SuccessMessageMixin, CreateView):
    template_name = "pages/home.html"
    form_class = JoinForm
    success_url = ('/')

    def get_context_data(self, *args, **kwrgs):
        context = super(HomeView, self).get_context_data(*args, **kwrgs)
        context['page_obj'] = Page.objects.filter(featured=True).first()
        return context


    def get_success_message(self, cleaned_data):
        return ("Thank You for join us")
#class HomeView(View):
 #   def get(self, request, *args, **kwrgs):
  #      return render(request, "pages/home.html", {})