from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('partner/<int:partner_id>/history/', views.PartnerHistory, name='partner_history'),
    path('add_partner', views.add_partner, name='add_partner'),
    path('partner/delete/<int:partner_id>/', views.delete_partner, name='delete_partner'),
    path('partner/update/<int:partner_id>/', views.update_partner, name='update_partner'),
    path('partner/update/<int:partner_id>/save/', views.update_partner_save, name='update_partner_save'),
]