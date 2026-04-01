from django.shortcuts import render
from .data import stat_cards,services,avis_list
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView

# Create your views here.
class HomePageView(TemplateView):
    template_name="home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['stat_cards']= stat_cards
        context['services']= services
        context['avis_list']= avis_list

        return context

class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name='registration/signup.html'



### def home(request):

#     context = {
#         'stat_cards': stat_cards,
#         'services': services,
#         'avis_list': avis_list,
#     }
    
#     return render(request,"home.html",context)