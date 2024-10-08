from django.shortcuts import render,redirect
from .models import Contact,Service,Realisation,Avis
from django.contrib import messages

def index(request):
    # Récupérer tous les services
    services = Service.objects.all()
    for service in services:
        service.is_external = service.link.startswith('http')

    # Récupérer toutes les réalisations
    realisations = Realisation.objects.all()

    # Récupérer tous les avis
    avis_list = Avis.objects.all()  # Récupérer tous les avis

    # Rendre le template avec les services, réalisations et avis
    return render(request, 'index.html', {
        'services': services,
        'realisations': realisations,
        'avis_list': avis_list  # Ajouter les avis à la context
    })


def apropos(request):
    return render(request, 'a-propos.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:  # Vérifie que tous les champs sont remplis
            contact = Contact(name=name, email=email, message=message)
            contact.save()  # Sauvegarde dans la base de données
            messages.success(request, 'Merci pour votre message. Nous vous répondrons bientôt.')
            return redirect('contact')  # Redirection après succès
        else:
            messages.error(request, 'Veuillez remplir tous les champs.')  # Message d'erreur si champs manquants
    
    return render(request, 'contact.html')  # Affiche le formulaire

def creationSiteWeb(request): 
    return render(request, 'creation-de-site-web.html')

def referencement(request):
    return render(request, 'referencement.html')  

def maintenance(request):
    return render(request, 'maintenance.html')    