from django.urls import path
from . import views  # Import views from the same app(core)

urlpatterns = [
    # Donation form page - shows form and handles submission
    path('donate/', views.create_donation, name='create_donation'),

    # Donation success page - shows after a successful donation
    path('donate/success/', views.donation_success, name='donation_success'),

    # Feeding report form page - shows form and handles submission
    path('feeding-report/', views.create_feeding_report, name='create_feeding_report'),

    # Feeding report success page
    path('feeding-report/success/', views.feeding_report_success, name='feeding_report_success'),

    # Event creation form page - shows form and handles submission
    path('event/create/', views.create_event, name='create_event'),

    # Event success page
    path('event/success/', views.event_success, name='event_success'),

    #This is for the root URL
    path('', views.homepage, name='homepage'),

    #Donor dashboard page
    path('dashboard/', views.donor_dashboard, name='donor_dashboard'),
    
    #Donations made by donor page
    path('donations/', views.donor_donations, name='donor_donations'),



]

