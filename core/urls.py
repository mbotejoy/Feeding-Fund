from django.urls import path
from . import views  # Import views from the same app(core)

urlpatterns = [
   
    # Donation success page - shows after a successful donation
    path('donate/success/', views.donation_success, name='donation_success'),

    #Donor dashboard view
    path('donor-dashboard/', views.donor_dashboard, name='donor_dashboard'),

    # Donation form view
    path('donate/', views.donation_form_view, name='donation_form'),

    # Event participation form view
    path('join-event/', views.event_participation_form_view, name='event_participation_form'),

    # Feeding report form page - shows form and handles submission
    path('feeding-report/', views.create_feeding_report, name='create_feeding_report'),

    # Feeding report success page
    path('feeding-report/success/', views.feeding_report_success, name='feeding_report_success'),

    # Event creation form page - shows form and handles submission
    path('event/create/', views.create_event, name='create_event'),

    # Event success page
    path('event/success/', views.event_success, name='event_success'),

    #This is for the homepage
    path('', views.homepage, name='homepage'),

    #Community Agent dashboard view
    path('communityagent-dashboard/', views.communityagent_dashboard, name='communityagent_dashboard'),

    path('register-school/', views.register_school, name='register_school'),
    
    path('submit_feeding_report/', views.submit_feeding_report, name='submit_feeding_report'),

    # Link for the signup page
    path('signup/', views.signup, name='signup'),

]

