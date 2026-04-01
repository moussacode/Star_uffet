import uuid
from django.db import models

# Create your models here.

class Specialite(models.Model):
    nom = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nom}"

class Traiteur(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nomcomplet = models.CharField(max_length=20)
    specialites = models.ManyToManyField(Specialite)
    experience = models.PositiveIntegerField()
    description = models.TextField()
    adresse = models.CharField(max_length=15)
    note = models.FloatField(default=0.0)
    est_actif = models.BooleanField(default=False)
    email = models.EmailField()
    datedecreation = models.DateTimeField(
        auto_now_add=True
    )
    telephone = models.CharField(max_length=10)
    image = models.ImageField(upload_to='traiteurs/')

    def __str__(self):
        return f"{self.nomcomplet}"