from django.http import HttpResponse
from django.contrib.auth.decorators import login_required          #Ensures the user is authenticated
from django.shortcuts import render, redirect, get_object_or_404
from .forms import (DonationForm, FeedingReportForm, EventForm, EventParticipationForm,UserForm, SchoolForm, FeedingReportForm)
from .models import (Donation, FeedingReport, Event, User, School)


# View to handle creation of a new Donation
from django.shortcuts import render, redirect
from .forms import DonationForm, EventParticipationForm  # Import your forms

# Show the donor dashboard
def donor_dashboard(request):
    return render(request, 'donor_dashboard.html')  # This is the dashboard home page

# Show the community_agent dashboard
def communityagent_dashboard(request):
    return render(request, 'communityagent_dashboard.html')


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


# View to handle submission of a Feeding Report
def create_feeding_report(request):
    """
    Display and process the Feeding Report form.
    On GET: renders an empty form.
    On POST: validates and saves the report, then redirects to success page.
    """
    if request.method == 'POST':
        form = FeedingReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feeding_report_success')
    else:
        form = FeedingReportForm()
    return render(request, 'foodfund/feeding_report_form.html', {'form': form})

# View to handle creation of a new Event
def create_event(request):
    """
    Display and process the Event creation form.
    On GET: renders an empty form.
    On POST: validates and saves the event, then redirects to success page.
    """
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_success')
    else:
        form = EventForm()
    return render(request, 'foodfund/event_form.html', {'form': form})

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


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            role_name = request.POST.get('role')  # from <select id="role">
            role = role.objects.get(name=role_name)
            user.role = role
            user.save()
            return redirect('nourished.html')# success page
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def register_school(request):
    return render(request, 'forms/register_school.html')

def submit_feeding_report(request):
    return render(request, 'forms/submit_feeding_report.html')

