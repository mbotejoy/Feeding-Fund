from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for creating a new donation
    # Maps to the create_donation view which handles the donation form
    path('donate/', views.create_donation, name='create_donation'),

    # URL pattern for the donation success page
    # Displays a confirmation message after successful donation submission
    path('donate/success/', views.donation_success, name='donation_success'),

    # URL pattern for submitting a feeding report
    # Maps to the create_feeding_report view which handles feeding report form
    path('feeding-report/', views.create_feeding_report, name='create_feeding_report'),

    # URL pattern for the feeding report success page
    # Displays confirmation after successful feeding report submission
    path('feeding-report/success/', views.feeding_report_success, name='feeding_report_success'),

    # URL pattern for creating a new event
    # Maps to the create_event view which handles event creation form
    path('event/create/', views.create_event, name='create_event'),

    # URL pattern for the event creation success page
    # Displays confirmation after successful event creation
    path('event/success/', views.event_success, name='event_success'),
]