from django.contrib import admin
from .models import Contact, Service, Realisation,Avis

admin.site.register(Contact)
admin.site.register(Service)

@admin.register(Realisation)  
class RealisationAdmin(admin.ModelAdmin):
    list_display = ('title',)  
    
@admin.register(Avis)
class AvisAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'contenu')
    search_fields = ('auteur', 'contenu')
