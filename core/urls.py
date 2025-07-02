from django.urls import path
from . import views  # Import views from the same app(core)

urlpatterns = [

    #Donor dashboard view
    path('donor-dashboard/', views.donor_dashboard, name='donor_dashboard'),

    # Donation form view
    path('donate/', views.donation_form_view, name='donation_form'),

    # Event creation form page - shows form and handles submission
    path('event/create/', views.create_event, name='create_event'),
    
    #This is for the homepage
    path('', views.homepage, name='homepage'),

    #This is for the About Us page
    path('', views.about_us, name='about_us'),

    #This is for the Impact page
    path('', views.impact, name='impact'),

    # Link for the signup page
    path('signup/', views.signup, name='signup'),

    # Link for the login page
    path('login/', views.login, name='login'),

    # Link for the School Admin Dashboard 
    path('school_admin-dashboard/', views.school_admin, name='school_admin'),

    #Community Agent dashboard view
    path('communityagent-dashboard/', views.communityagent_dashboard, name='communityagent_dashboard'),

    #Parent dashboard view
    path('parent-dashboard/', views.parent, name='parent'),

    #Parent dashboard view
    path('register-child/', views.register_child, name='register_child'),

    #Community Agent is able to register a school
    path('register-school/', views.register_school, name='register_school'),
    
    #Community Agent submits these reports
    path('feeding-report/', views.submit_feeding_report, name='submit_feeding_report'),

    #Link to Attendace form
    path('attendance/', views.attendance, name='attendance'),

    #School Admin/Teacher creates the reports
    path('create-feeding-report/', views.create_feeding_report, name='create_feeding_report'),

    #View of the event participation
    path('join-an-event/', views.join_an_event, name='join_an_event'),

    #View of the feedback form
    path('feedback/', views.give_feedback, name='give_feedback'),

    path('attendance_records/', views.attendance_records, name='attendance_records'),

        # Edit and Delete routes for attendance records
    path('attendance/edit/<int:record_id>/', views.edit_attendance, name='edit_attendance'),
    path('attendance/delete/<int:record_id>/', views.delete_attendance, name='delete_attendance'),




]

