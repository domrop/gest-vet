
from django.urls import path
from django.urls import include, re_path

from . import views

'''
urlpatterns = [
    path('', views.index, name='index'),
    path('pazienti/', views.PazientiListView.as_view(), name='pazienti'),
    path('pazienti/<int:pk>', views.PazientiDetailView.as_view(), name='pazienti-detail'),
    path('pazienti/create/', views.PazientiCreate.as_view(), name='nuovascheda'),
    path('pazienti/<int:pk>/update/', views.PazientiUpdate.as_view(), name='pazienti_update'),
    #re_path(r'^pazienti/(?P<pk>\d+)/update/$', views.PazientiUpdate.as_view(), name='pazienti_update'),
    #path('pazienti/<slug:pk>/update/', views.PazientiUpdate.as_view(), name='pazienti_update'),
    path('pazienti/<int:pk>/delete/', views.PazientiDelete.as_view(), name='cancellascheda')
]
'''
urlpatterns = [
    path('', views.index, name='index'),
    path('pazienti/', views.PazientiListView.as_view(), name='pazienti'),
    path('pazienti/<int:pk>', views.PazientiDetailView.as_view(), name='pazienti-detail'),
    path('nuovascheda/', views.PazientiCreate.as_view(), name='nuovascheda'),
    path('pazienti/<int:pk>/update/', views.PazientiUpdate.as_view(), name='pazienti_update'),
    path('pazienti/<int:pk>/delete/', views.PazientiDelete.as_view(), name='cancellascheda'),
    path('dettaglio_paziente/<int:pk>', views.dettaglio_paziente, name='dettaglio_paziente'),
    path('nuova_visita/<int:pk>', views.VisitaCreate.as_view(), name='nuova_visita'),
    path('edit_visita/<int:pk>', views.VisitaUpdate.as_view(), name='edit_visita'),
    path('visite/<int:pk>/delete/', views.VisitaDelete.as_view(), name='visitacancellascheda'),
    #path('dettaglio_paziente/<int:pk>', views.VisitaDelete.as_view(), name='dettaglio_paziente'),
]

