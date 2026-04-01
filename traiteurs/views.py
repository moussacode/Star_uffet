from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from . import models
# Create your views here.
from .form import DevenirTraiteurForm

def traiteurs(request):

    traiteurs = models.Traiteur.objects.all()
    specialites = models.Specialite.objects.all()
    contexte ={
        'traiteurs': traiteurs,
        'specialites':specialites 
    }
    
    return render(request,"traiteurs.html",contexte)

def detail_traiteurs (request,pk):
    traiteur = get_object_or_404(models.Traiteur,pk=pk) 
    contexte={
        'traiteur':traiteur
    }
    return render(request,"detail-traiteur.html",contexte)

@login_required
def inscription_traiteur (request):
    success_msg =None
    if request.method == 'POST':
        form = DevenirTraiteurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            success_msg='Success'
            form = DevenirTraiteurForm()
        else :
            print()
    else:
        form = DevenirTraiteurForm()
    context = {
        'form': form,
        'success_msg':success_msg
    }
    return render(request,"inscription-traiteur.html",context)