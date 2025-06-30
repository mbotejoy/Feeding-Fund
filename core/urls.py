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

    # Feeding report success page
    path('feeding-report/success/', views.feeding_report_success, name='feeding_report_success'),

    # Event creation form page - shows form and handles submission
    path('event/create/', views.create_event, name='create_event'),

    # Event success page
    path('event/success/', views.event_success, name='event_success'),

    #This is for the homepage
    path('', views.homepage, name='homepage'),

    #This is for the About Us page
    path('', views.about_us, name='about_us'),

    #This is for the Impact page
    path('', views.impact, name='impact'),

    # Link for the signup page
    path('signup/', views.signup, name='signup'),

    # Link for the School Admin Dashboard 
    path('school_admin-dashboard/', views.school_admin, name='school_admin'),

    #Community Agent dashboard view
    path('communityagent-dashboard/', views.communityagent_dashboard, name='communityagent_dashboard'),

    #Parent dashboard view
    path('parent-dashboard/', views.parent, name='parent'),

    path('register-school/', views.register_school, name='register_school'),
    
    #Community Agent submits these reports
    path('feeding-report/', views.submit_feeding_report, name='submit_feeding_report'),




]

