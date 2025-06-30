from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.decorators import login_required          #Ensures the user is authenticated
from django.shortcuts import render, redirect, get_object_or_404
from .forms import (DonationForm, FeedingReportForm, EventForm, EventParticipationForm,UserForm, SchoolForm, FeedingReportForm,StudentForm,AttendanceForm)
from .models import (Donation, FeedingReport, Event, User, School,Role,Student,Attendance)



#
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            messages.success(request, 'Registration successful!')
            return redirect('homepage')  # Make sure 'homepage' URL name exists
        else:
            print("FORM ERRORS:", form.errors)
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'forms/user.html', {'form': form, 'errors': form.errors})
    else:
        form = UserForm()
        return render(request, 'forms/user.html', {'form': form})
    
    #View of the submission of a feeding report
def submit_feeding_report(request):
    if request.method == 'POST':
        form = FeedingReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Feeding report submitted successfully!")
            return redirect('communityagent_dashboard')
    else:
        form = FeedingReportForm()
    return render(request, 'forms/feeding_report.html', {'form': form})

#View to handle registering of a school
def register_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered School Successfully!")
            return redirect('communityagent_dashboard')
    else:
        form = SchoolForm()
    return render(request, 'forms/school.html', {'form': form})


# View to handle creation of a new Event
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event Created  Successfully!")
            return redirect('communityagent_dashboard')
    else:
        form = EventForm()
    return render(request, 'forms/event.html', {'form': form})

# View to handle registration of a child by a parent
def register_child(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Child Registered Successfully!")
            return redirect('parent')
    else:
        form = StudentForm()
    return render(request, 'forms/student.html', {'form': form})

# View to handle attendance
def attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Recorded Student Attendance Successfully!")
            return redirect('school_admin')
    else:
        form = AttendanceForm()
    return render(request, 'forms/attendance.html', {'form': form})

    #View of the submission of a feeding report
def create_feeding_report(request):
    if request.method == 'POST':
        form = FeedingReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Feeding Report Created Successfully!")
            return redirect('school_admin')
    else:
        form = FeedingReportForm()
    return render(request, 'forms/feeding_report.html', {'form': form})




# Show the donor dashboard
def donor_dashboard(request):
    return render(request, 'donor_dashboard.html')  # This is the dashboard home page

# Show the community_agent dashboard
def communityagent_dashboard(request):
    return render(request, 'communityagent_dashboard.html')

# Show the school admin dashboard
def school_admin(request):
    return render(request, 'teacher.html')

# Show the parent dashboard
def parent(request):
    return render(request, 'parent.html')





# Handle donation form
def donation_form_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the donation to the database
            return redirect('donor_dashboard')  # Redirect after successful submission
    else:
        form = DonationForm()  # Create an empty form for GET request

    return render(request, 'templates/forms/donation_form.html', {'form': form})  # Render the form template

# Handle event participation form
def event_participation_form_view(request):
    if request.method == 'POST':
        form = EventParticipationForm(request.POST)
        if form.is_valid():
            form.save()  # Save event participation
            return redirect('donor_dashboard')  # Redirect to dashboard after submission
    else:
        form = EventParticipationForm()  # Display blank form for GET request

    return render(request, 'forms/event_participation_form.html', {'form': form})  # Render the form template




# Simple success page for Donation submission
def donation_success(request):
    """
    Render a success message after a donation is submitted.
    """
    return render(request, 'foodfund/success.html', {'message': 'Donation submitted successfully!'})

# Simple success page for Feeding Report submission
def feeding_report_success(request):
    """
    Render a success message after a feeding report is submitted.
    """
    return render(request, 'foodfund/success.html', {'message': 'Feeding report submitted successfully!'})

# Simple success page for Event creation
def event_success(request):
    """
    Render a success message after an event is created.
    """
    return render(request, 'foodfund/success.html', {'message': 'Event created successfully!'})

#Takes to home page
def homepage(request):
    return render(request, 'forms/nourished.html')

#About Us Page
def about_us(request):
    return render(request, 'forms/nourished.html')

#Impact Page
def impact(request):
    return render(request, 'forms/nourished.html')





