from django.urls import path
from app.views import *

urlpatterns = [
    path('', Index, name='index'),

    # Reports:
    path('reports/hoto-report/', Reports_Hoto, name='hoto_report'),
    
    path('reports/energy-drf/', DRFReport.as_view(), name='atc_site_report'),
    path('reports/energy-fuel-drawn/', FuelDrawnReport.as_view(), name='fuel_drawn'),
    path('reports/energy-energy-reading/', EnergyReadingReport.as_view(), name='diesel_filling'),

    # Forms:
    path('forms/diesel-meter/filling-reading-fill-form/', DieselFillingOrReadingViews.as_view(), name='atcform'),
    path('forms/fuel-drawn-fill-form/', FuelDrawnViews.as_view(), name='fueldrawnform'),

    path('user/logout/', LogOut.as_view(), name='logout'),
]