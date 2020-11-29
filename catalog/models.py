
from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns



#Lista pazienti
class Pazienti(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    nome_paziente = models.CharField('nome paziente', max_length=50, blank=True, null=True, default="")
    razza_paziente = models.CharField('razza paziente',max_length=50, primary_key=False, blank=True, null=True, default="")
    data_nascita_paziente = models.DateField('data_nascita_paziente', default="")
    nome_proprietario = models.CharField('nome proprietario',max_length=100, primary_key=False, blank=True, null=True, default="")
    cognome_proprietario = models.CharField('cognome proprietario',max_length=100, primary_key=False, blank=True, null=True, default="")
    telefono_proprietario = models.CharField('telefono proprietario',max_length=100, primary_key=False, blank=True, null=True, default="")
    email_proprietario = models.EmailField('email proprietario',max_length=100, primary_key=False, blank=True, null=True, default="")
    
    class Meta:
        ordering = ['nome_paziente']
        
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('pazienti-detail', args=[str(self.id)])
        
    def get_update_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('pazienti_update', args=[str(self.id)])
     
    def get_create_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('nuovascheda', args=[str(self.id)])
        
    def get_delete_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('cancellascheda', args=[str(self.id)])
        
    def __str__(self):
        """String for representing the Model object."""
        return self.nome_paziente
#CHIUSO Lista pazienti

class Visite(models.Model):
    idPaziente = models.ForeignKey(Pazienti, on_delete=models.CASCADE, null=False)
    data_visita = models.DateTimeField(default=None, null=False)
    anamnesi = models.CharField('anamnesi', max_length=2048, blank=True, null=True, default="")
    prognosi = models.CharField('prognosi', max_length=2048, blank=True, null=True, default="")
    prescrizioni = models.CharField('prescrizioni', max_length=2048, blank=True, null=True, default="")
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('dettaglio_paziente', args=[str(self.idPaziente.id)])    
    
    def get_delete_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('visitacancellascheda', args=[str(self.idPaziente.id)])