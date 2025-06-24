from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import (DonationForm, FeedingReportForm, EventForm, EventParticipationForm,UserForm)
from .models import (Donation, FeedingReport, Event,User)


# View to handle creation of a new Donation
from django.shortcuts import render, redirect
from .forms import DonationForm, EventParticipationForm  # Import your forms

# Show the donor dashboard
def donor_dashboard(request):
    return render(request, 'donor_dashboard.html')  # This is the dashboard home page

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
#Displays a message on the root URL
def homepage(request):
    return HttpResponse("Welcome to the Food Funding App!")



def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nourished.html')  # Make sure to define this URL or template
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})
