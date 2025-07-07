from django.shortcuts import render, redirect
from django.contrib import messages
from .forms_manual_mpesa import ManualMpesaDonationForm

# Manual MPESA donation view

def manual_mpesa_donation(request):
    if request.method == 'POST':
        form = ManualMpesaDonationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your donation details have been submitted. We will verify and contact you if needed.')
            return redirect('manual_mpesa_donation')
    else:
        form = ManualMpesaDonationForm()
    return render(request, 'forms/manual_mpesa_donation.html', {'form': form})
