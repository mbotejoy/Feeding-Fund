from django.urls import path
from . import views  # Import views from the same app(core)
from .views import manual_mpesa_donation, donor_donation_history

urlpatterns = [

    #Donor dashboard view
    path('donor-dashboard/', views.donor_dashboard, name='donor_dashboard'),

    # Donation form view
    path('mpesa/donate/', views.donation_form, name='donation_form'),

    # Manual MPESA donation form
    path('donate/manual/', manual_mpesa_donation, name='manual_mpesa_donation'),

    # Event creation form page - shows form and handles submission
    path('event/create/', views.create_event, name='create_event'),
    
    #This is for the homepage
    path('', views.homepage, name='homepage'),

    #This is for the About Us page
    path('about-us/', views.about_us, name='about_us'),

    #This is for the Impact page
    path('impact/', views.impact, name='impact'),

    # Link for the signup page
    path('signup/', views.signup, name='signup'),

    # Link for the login page
    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

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

    path('events/table/', views.events_table, name='events_table'),

    path('events/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),

            # Edit and Delete routes for student records
    path('student/edit/<int:record_id>/', views.edit_student_record, name='edit_student_record'),
    path('student/delete/<int:record_id>/', views.delete_student_record, name='delete_student_record'),

    path('stk-push/', views.stk_push, name='stk_push'),

    #Mpesa callback url
    path('mpesa/callback/', views.mpesa_callback, name='mpesa_callback'),

    path('student/<int:student_id>/toggle-active/', views.toggle_student_active, name='toggle_student_active'),

    # Donor's donation history page
    path('donor/donations/', views.donor_donation_history, name='donor_donation_history'),

    path('parent/update-wallet/', views.update_child_wallet, name='update_child_wallet'),

    path('parent/view-wallet/', views.view_child_wallet, name='view_child_wallet'),

    # Homepage MPESA donation form submission
    path('homepage-mpesa-donation/', views.homepage_mpesa_donation, name='homepage_mpesa_donation'),

    # Donation thank you page
    path('donation-thank-you/', views.homepage_donation_thankyou, name='homepage_donation_thankyou'),

]

