from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pazienti, Visite
from django.utils import timezone


def index(request):
    
    num_books = Pazienti.objects.all().count()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_pazienti': num_books, 
                 'num_visits': num_visits},
    )


from django.views import generic


class PazientiListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view for a list of books."""
    model = Pazienti
    paginate_by = 10
    permission_required = 'catalog.can_mark_returned'
    
class PazientiDetailView(PermissionRequiredMixin, generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Pazienti
    permission_required = 'catalog.can_mark_returned'
    
class PazientiCreate(PermissionRequiredMixin, CreateView):
    model = Pazienti
    fields = ['nome_paziente','razza_paziente','data_nascita_paziente','nome_proprietario','cognome_proprietario','telefono_proprietario','email_proprietario']
    template_name_suffix = '_nuovascheda'
    permission_required = 'catalog.can_mark_returned'
class PazientiUpdate(PermissionRequiredMixin, UpdateView):
    model = Pazienti
    fields = ['nome_paziente','razza_paziente','data_nascita_paziente','nome_proprietario','cognome_proprietario','telefono_proprietario','email_proprietario']
    permission_required = 'catalog.can_mark_returned'
    
class PazientiDelete(PermissionRequiredMixin, DeleteView):
    model = Pazienti
    success_url = reverse_lazy('pazienti')
    permission_required = 'catalog.can_mark_returned'
    
def dettaglio_paziente( request, pk ):
    pazienti = Pazienti.objects.get( pk = pk )
    visite = Visite.objects.filter( idPaziente=pazienti.id )
    return render(request, 'catalog/pazienti_detail.html', {'pazienti': pazienti, 'visite':visite})
    
def nuova_visita( request, pk ):
    visita = Visite()
    visita.data_visita = timezone.now()
    visita.idPaziente=Pazienti.objects.get( pk = pk )
    visita.anamnesi = ""
    visita.prognosi = ""
    visita.prescrizioni = ""
    visita.save()
    return redirect('dettaglio_paziente', pk = pk)
    
class VisitaUpdate(UpdateView):
    model = Visite
    fields = ['anamnesi','prognosi','prescrizioni']
    template_name_suffix = '_update_form'
    

    
class VisitaCreate(CreateView):
    model = Visite
    fields = ['anamnesi','prognosi','prescrizioni']
    template_name_suffix = '_create_form'
    
    def form_valid(self, form):
        idPaziente = get_object_or_404(Pazienti, pk=self.kwargs['pk'])
        form.instance.idPaziente = idPaziente
        form.instance.data_visita = timezone.now()
        return super(VisitaCreate, self).form_valid(form)    

'''
class VisitaDelete(PermissionRequiredMixin, DeleteView):
    model = Visite
    success_url = reverse_lazy('index')
    permission_required = 'catalog.can_mark_returned'
  
'''
class VisitaDelete(PermissionRequiredMixin, DeleteView):
    model = Visite
    success_url = reverse_lazy('dettaglio_paziente')
    permission_required = 'catalog.can_mark_returned'
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('dettaglio_paziente', args=[str(self.idPaziente.id)])
    '''
    def get_success_url(self):
          # if you are passing 'pk' from 'urls' to 'DeleteView' for company
          # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
          pazienteid = self.kwargs['pk']
          return reverse_lazy('dettaglio_paziente', kwargs={'pk': dettaglio_paziente})
  '''