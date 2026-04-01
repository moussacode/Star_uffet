from django.contrib import admin
from .models import Traiteur, Specialite



class TraiteurAdmin(admin.ModelAdmin):
    list_display=(
        'nomcomplet',
        'email',
        'telephone',
        'datedecreation'
    )

admin.site.register(Traiteur,TraiteurAdmin)
admin.site.register(Specialite)
# Register your models here.
