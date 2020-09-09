from django.urls import path
from django.conf.urls import url
from EOlive.models import User, evidencijagospodarstva, berba, podaci_radnje, prihranjivanje, spricanje

from .views import  userListView, userDetailView, evidencijagospodarstvaListView, berbaListView, podaci_radnjeListView, prihranjivanjeListView, spricanjeListView, evidencijagospodarstvaDetailView, berbaDetailView, podaci_radnjeDetailView, prihranjivanjeDetailView, spricanjeDetailView, evidencijagospodarstvaCreateView, berbaCreateView, podaci_radnjeCreateView, prihranjivanjeCreateView, spricanjeCreateView, evidencijagospodarstvaDeleteView, berbaDeleteView, podaci_radnjeDeleteView, prihranjivanjeDeleteView, spricanjeDeleteView, evidencijagospodarstvaUpdateView, berbaUpdateView, podaci_radnjeUpdateView, prihranjivanjeUpdateView, spricanjeUpdateView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('User/', userListView),
    path('User/<int:pk>', userDetailView),
    path('Evidencija/', evidencijagospodarstvaListView.as_view()),
    path('Evidencija/create/', evidencijagospodarstvaCreateView.as_view()),
    path('Evidencija/<int:pk>', evidencijagospodarstvaDetailView.as_view()),
    path('Berba/', berbaListView.as_view()),
    path('Berba/create/', berbaCreateView.as_view()),
    path('Berba/<int:pk>', berbaDetailView.as_view()),
    path('Berba/<int:pk>/update', berbaUpdateView.as_view()),
    path('Berba/<int:pk>/delete', berbaDeleteView.as_view()),
    path('PodaciRadnje/', podaci_radnjeListView.as_view()),
    path('PodaciRadnje/create/', podaci_radnjeCreateView.as_view()),
    path('PodaciRadnje/<int:pk>', podaci_radnjeDetailView.as_view()),
    path('PodaciRadnje/<int:pk>/update', podaci_radnjeUpdateView.as_view()),
    path('PodaciRadnje/<int:pk>/delete', podaci_radnjeDeleteView.as_view()),
    path('Prihranjivanje/', prihranjivanjeListView.as_view()),
    path('Prihranjivanje/create/', prihranjivanjeCreateView.as_view()),
    path('Prihranjivanje/<int:pk>', prihranjivanjeDetailView.as_view()),
    path('Prihranjivanje/<int:pk>/update', prihranjivanjeUpdateView.as_view()),
    path('Prihranjivanje/<int:pk>/delete', prihranjivanjeDeleteView.as_view()),
    path('Spricanje/', spricanjeListView.as_view()),
    path('Spricanje/create/', spricanjeCreateView.as_view()),
    path('Spricanje/<int:pk>', spricanjeDetailView.as_view()),
    path('Spricanje/<int:pk>/update', spricanjeUpdateView.as_view()),
    path('Spricanje/<int:pk>/delete', spricanjeDeleteView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)