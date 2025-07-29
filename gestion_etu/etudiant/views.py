from django.shortcuts import render, HttpResponseRedirect
from .forms import Student_registrations
from .models import User


# Create your views here.
def show(request):
    if request.method == 'POST':
        fm =Student_registrations(request.POST)
        #insertion dans la data base
        if fm.is_valid():
            #apres insertion dans la database nettoyer les champs 
            nettoyer_nom= fm.cleaned_data['name']
            nettoyer_email= fm.cleaned_data['email']
            nettoyer_password= fm.cleaned_data['password']
            reg= User(name=nettoyer_nom, email=nettoyer_email, password=nettoyer_password)
            reg.save()
            fm= Student_registrations()
    else:
        fm =Student_registrations() 
    # recuperation et affichage des donnees de la base de donnee
    student= User.objects.all()
    return render(request, 'etudiant/affichage.html', {'form':fm, 'etudiant':student})

#function for destroy the data in database
def delete(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk= id)
        pi.delete()
        return HttpResponseRedirect('/enregistrement/')
    
#mise a jour des informations d'un user    
def update(request, id):
    if(request.method == 'POST'):
        pi= User.objects.get(pk=id)
        fm= Student_registrations(request.POST , instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm= Student_registrations(instance=id)    
    return render(request, 'etudiant/update.html', {'form':fm})