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
    student= User.objects.all()
    return render(request, 'etudiant/affichage.html', {'form':fm, 'etudiant':student})

#function for destroy the data in database
def delete(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk= id)
        pi.delete()
        return HttpResponseRedirect('/enregistrement/')