from django.http import HttpResponse
from django.contrib.auth.decorators import login_required          #Ensures the user is authenticated
from django.shortcuts import render, redirect, get_object_or_404
from .forms import (DonationForm, FeedingReportForm, EventForm)
from .models import (Donation, FeedingReport, Event)


# View to handle creation of a new Donation
def create_donation(request):
    """
    Display and process the Donation form.
    On GET: renders an empty form.
    On POST: validates and saves the donation, then redirects to success page.
    """
    if request.method == 'POST':
        form = DonationForm(request.POST)  # Bind form with POST data
        if form.is_valid():
            form.save()  # Save the valid donation instance
            return redirect('donation_success')  # Redirect to success confirmation page
    else:
        form = DonationForm()  # Unbound form for GET request
    # Render the donation form template with the form context
    return render(request, 'foodfund/donation_form.html', {'form': form})

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
    return render(request, 'foodfund/nourished.html')
#View for the donor dashboard page
#Only logged in users can access this page
@login_required
def donor_dashboard(request):
    return render(request, 'foodfund/dashboard.html')

def donor_donations(request):
    # Filter donations where the donor is the logged-in user
    donations = Donation.objects.filter(donor=request.user)
    # Render the donation list template with the filtered donations
    return render(request, 'foodfund/donor_donations.html', {'donations': donations})

def donation_receipt(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id)
    return render(request, 'donation_receipt.html', {'donation': donation})

