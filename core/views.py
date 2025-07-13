from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from datetime import datetime
import base64
import requests  # Added import for requests
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import authenticate,logout, login as auth_login
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required          #Ensures the user is authenticated
from django.shortcuts import render, redirect, get_object_or_404
from core.forms import (DonationForm, FeedingReportForm, EventForm, EventParticipationForm,UserForm, SchoolForm, FeedingReportForm,StudentForm,AttendanceForm,FeedbackForm,ManualMpesaDonationForm)
from core.models import (Donation, FeedingReport, Event, User, School,Role,Student,Attendance, ManualMpesaDonation, WalletTopUp, ChildWallet, EventParticipation)


#View of the User Registration page
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            # Do not set role here; admin will assign role later
            user.save()
            messages.success(request, 'Registration successful! Awaiting verification by admin. Please log in after approval.')
            return redirect('homepage')  # Redirect to home page after registration
        else:
            print("FORM ERRORS:", form.errors)
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'forms/user.html', {'form': form, 'errors': form.errors})
    else:
        form = UserForm()
        return render(request, 'forms/user.html', {'form': form})
    

#login view    
def login_view(request):
    if request.method == 'POST':
        # Get the submitted values from the login form
        email = request.POST.get('username')  # full name field used as username
        password = request.POST.get('password')   # Password field

        try:
            # Try to retrieve the user from the database using email
            user = User.objects.get(email=email)

            # Check if the entered password matches the user's stored hashed password
            if check_password(password, user.password):
                if not user.is_verified:
                    messages.error(request, 'Your account is not verified. Please wait for admin approval.')
                    return redirect('homepage')
                if not user.role:
                    messages.error(request, 'Your account does not have a role assigned. Please contact the admin.')
                    return redirect('homepage')
                # If password is correct, user is verified, and has a role, log in the user manually
                auth_login(request, user)

                # Redirect the user to the appropriate dashboard based on their role
                role = user.role.name.strip().lower()

                if role == 'donor':
                    return redirect('donor_dashboard')
                elif role == 'school admin':
                    return redirect('school_admin')
                elif role == 'community agent':
                    return redirect('communityagent_dashboard')
                elif role == 'parent':
                    return redirect('parent')
                else:
                    # If role is not matched, go to homepage
                    return redirect('homepage')

            else:
                # If the password is incorrect, show an error message and redirect to homepage
                messages.error(request, 'Invalid password.')
                return redirect('homepage')

        except User.DoesNotExist:
            # If no user with that email exists, show an error and redirect to homepage
            messages.error(request, 'User with that email does not exist.')
            return redirect('homepage')

    # If GET request, show the login form
    return render(request, 'forms/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('homepage')  # This sends the user back to the login page
    
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
        form = EventForm(request.POST, user=request.user)
        if form.is_valid():
            event = form.save(commit=False)
            if request.user.role and request.user.role.name.lower() == 'school admin':
                event.school = request.user.school  # Auto-assign school
            event.created_by = request.user  # Always set the creator to the logged-in user
            event.save()
            messages.success(request, "Event Created  Successfully!")
            return redirect('communityagent_dashboard')
    else:
        form = EventForm(user=request.user)
    return render(request, 'forms/event.html', {'form': form, 'user': request.user})

# View to handle registration of a child by a parent
def register_child(request):
    if request.method == 'POST':
        #allow the logged in parent to automatcally register their child
        form = StudentForm(request.POST, parent=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Child Registered Successfully!")
            return redirect('parent')
    else:
        form = StudentForm(parent=request.user)
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
        form = FeedingReportForm(request.POST, user=request.user)
        if form.is_valid():
            report = form.save(commit=False)
            if request.user.role and request.user.role.name.lower() == 'school admin':
                report.school = request.user.school  # Auto-assign school
            report.save()
            messages.success(request, "Feeding Report Created Successfully!")
            return redirect('school_admin')
    else:
        form = FeedingReportForm(user=request.user)
    return render(request, 'forms/feeding_report.html', {'form': form})


# Handle event participation form
def join_an_event(request):
    if request.method == 'POST':
        form = EventParticipationForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully joined the event!")
            return redirect('donor_dashboard')
    else:
        form = EventParticipationForm(user=request.user)
    return render(request, 'forms/event_participation.html', {'form': form, 'donor': request.user})  # Render the form template

# Handles Feedback form
def give_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save feedback
            messages.success(request, "Feedback Sent Successfully!")
            return redirect('homepage')  # Redirect to dashboard after submission
    else:
        form = FeedbackForm()  # Display blank form for GET request

    return render(request, 'forms/feedback.html', {'form': form})  # Render the form template




# Show the donor dashboard
@login_required
def donor_dashboard(request):
    role_name = str(request.user.role.name).strip().lower() if request.user.role else None
    if role_name != 'donor':
        messages.error(request, f'Unauthorized access. Your role: {role_name!r}')
        return redirect('homepage')
    feeding_reports = FeedingReport.objects.all().order_by('-report_date')[:20]  # Show latest 20 reports
    context = {
        'feeding_reports': feeding_reports,
    }
    return render(request, 'donor_dashboard.html', context)

# Show the community_agent dashboard
@login_required
def communityagent_dashboard(request):
    role_name = str(request.user.role.name).strip().lower() if request.user.role else None
    if role_name != 'community agent':
        messages.error(request, f'Unauthorized access. Your role: {role_name!r}')
        return redirect('homepage')
    student_records = Student.objects.all()
    events = Event.objects.all()
    attendance_records = Attendance.objects.select_related('student__school').all()
    context = {
        'student_records': student_records,
        'events': events,
        'attendance_records': attendance_records,
    }
    return render(request, 'communityagent_dashboard.html', context)

# Show the school admin dashboard
@login_required
def school_admin(request):
    role_name = str(request.user.role.name).strip().lower() if request.user.role else None
    if role_name != 'school admin':
        messages.error(request, f'Unauthorized access. Your role: {role_name!r}')
        return redirect('homepage')
    attendance_records = Attendance.objects.select_related('student__school').all()
    students = Student.objects.filter(school=request.user.school)
    return render(request, 'teacher.html', {
        'attendance_records': attendance_records,
        'students': students
    })

# Show the parent dashboard
@login_required
def parent(request):
    role_name = str(request.user.role.name).strip().lower() if request.user.role else None
    if role_name != 'parent':
        messages.error(request, f'Unauthorized access. Your role: {role_name!r}')
        return redirect('homepage')
    return render(request, 'parent.html')


#Takes to home page
def homepage(request):
        events = Event.objects.all()  # Fetch all events
        return render(request, 'forms/nourished.html', {'events': events})


#About Us Page
def about_us(request):
    return render(request, 'forms/nourished.html')

#Impact Page
def impact(request):
    return render(request, 'forms/nourished.html')



# Handle donation form
def donation_form(request):
    schools = School.objects.all()

    if request.method == 'POST':
        form = ManualMpesaDonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            if request.user.is_authenticated:
                donation.user = request.user
            donation.save()
            messages.success(request, 'Thank you! Your donation details have been submitted. We will verify and contact you if needed.')
            return redirect('donor_donation_history')
    else:
        form = ManualMpesaDonationForm()

    return render(request, 'forms/donation_form.html', {
        'form': form,
        'schools': schools
    })

def attendance_records(request):
    # Fetch all attendance records from the database
    attendance_records = Attendance.objects.all()

    # Pass the records to the template
    return render(request, 'attendance/communityagent_dashboard.html', {'attendance_records': attendance_records})

# View to edit a single attendance record
def edit_attendance(request, record_id):
    # Get the attendance record or return 404 if not found
    record = get_object_or_404(Attendance, id=record_id)

    if request.method == 'POST':
        # If form submitted, populate it with POST data and the instance
        form = AttendanceForm(request.POST, instance=record)
        if form.is_valid():
            form.save()  # Save the updated record
            messages.success(request, "Attendance record updated successfully.")
            return redirect('communityagent_dashboard')  # Redirect back to dashboard
    else:
        # If GET request, display the form with the current record
        form = AttendanceForm(instance=record)

    # Render edit page
    return render(request, 'forms/edit_attendance.html', {'form': form})


# View to delete a single attendance record
def delete_attendance(request, record_id):
    record = get_object_or_404(Attendance, id=record_id)  # Get record or 404
    if request.method == 'POST':
        record.delete()  # Delete the record
        messages.success(request, "Attendance record deleted.")
        return redirect('communityagent_dashboard')

    # Optional confirmation page 
    return render(request, 'forms/confirm_delete.html', {'record': record})


def events_table(request):
    events = Event.objects.all()
    return render(request, 'forms/nourished.html', {'events': events})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('homepage')  # Or wherever your event list is shown
    else:
        form = EventForm(instance=event)

    return render(request, 'forms/edit_event.html', {'form': form, 'event': event})

# View to delete a single attendance record
def delete_event(request, event_id):
    record = get_object_or_404(Event, id=event_id)  # Get record or 404
    if request.method == 'POST':
        record.delete()  # Delete the record
        messages.success(request, "Event deleted Successfully.")
        return redirect('homepage')

    # Optional confirmation page 
    return render(request, 'forms/confirm_delete.html', {'record': record})

# View to edit student records
def edit_student_record(request, record_id):
    # Get the attendance record or return 404 if not found
    record = get_object_or_404(Student, id=record_id)

    if request.method == 'POST':
        # If form submitted, populate it with POST data and the instance
        form = StudentForm(request.POST, instance=record)
        if form.is_valid():
            form.save()  # Save the updated record
            messages.success(request, "Student record updated successfully.")
            return redirect('communityagent_dashboard')  # Redirect back to dashboard
    else:
        # If GET request, display the form with the current record
        form = AttendanceForm(instance=record)

    # Render edit page
    return render(request, 'forms/edit_student.html', {'form': form})

# View to delete student record
def delete_student_record(request, record_id):
    record = get_object_or_404(Student, id=record_id)  # Get record or 404
    if request.method == 'POST':
        record.delete()  # Delete the record
        messages.success(request, "Event deleted Successfully.")
        return redirect('communityagent_dashboard')

    # Optional confirmation page 
    return render(request, 'forms/delete_student.html', {'record': record})

def get_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(
        url,
        auth=(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET)
    )

    if not response.ok or not response.text.strip():
        raise Exception(f"MPESA OAuth Error: {response.status_code} {response.text[:200]}")

    try:
        data = response.json()
        return data['access_token']
    except Exception as e:
        raise Exception(f"Failed to decode access token response: {e}, Raw response: {response.text[:200]}")


#Mpesa Integration
@csrf_exempt
def stk_push(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        donor_name = request.POST.get('donor_name')
        school = request.POST.get('school')

        # Format phone
        if phone.startswith('0'):
            phone = phone.replace('0', '254', 1)

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        password = base64.b64encode((settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + timestamp).encode()).decode()

        payload = {
            "BusinessShortCode": settings.MPESA_SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": settings.MPESA_SHORTCODE,
            "PhoneNumber": phone,
            "CallBackURL": settings.MPESA_CALLBACK_URL,
            "AccountReference": school,
            "TransactionDesc": f"Donation by {donor_name} to {school}"
        }

        headers = {
            "Authorization": f"Bearer {get_access_token()}",
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        response = requests.post(url, json=payload, headers=headers)

        # Defensive: check for empty or non-OK response
        if not response.ok or not response.text.strip():
            messages.error(request, f"No response or error from MPESA server. Status: {response.status_code}")
            return render(request, "forms/donation_form.html", {"form": DonationForm(), "schools": School.objects.all()})

        # Check if response is JSON
        content_type = response.headers.get('Content-Type', '')
        if 'application/json' not in content_type:
            messages.error(request, f"MPESA server did not return JSON. Status: {response.status_code}. Response: {response.text[:200]}")
            return render(request, "forms/donation_form.html", {"form": DonationForm(), "schools": School.objects.all()})

        try:
            resp_json = response.json()
        except Exception:
            messages.error(request, f"Failed to decode MPESA response: {response.text[:200]}")
            return render(request, "forms/donation_form.html", {"form": DonationForm(), "schools": School.objects.all()})

        # Check for success
        if response.status_code == 200 and resp_json.get('ResponseCode') == '0':
            messages.success(request, "MPESA payment initiated. Complete the payment on your phone.")
            return render(request, "donation_success.html", {"response": resp_json})
        else:
            error_message = resp_json.get('errorMessage', f'Failed to initiate MPESA payment. Status: {response.status_code}. Response: {response.text[:200]}')
            messages.error(request, error_message)
            return render(request, "forms/donation_form.html", {"form": DonationForm(), "schools": School.objects.all()})

    # If GET, redirect to donation form
    return redirect('donation_form')
    
@csrf_exempt
def mpesa_callback(request):
    print("Callback received:", request.body)
    return JsonResponse({"status": "received"})

@login_required
def toggle_student_active(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.is_active = not student.is_active
    student.save()
    status = "activated" if student.is_active else "deactivated"
    messages.success(request, f"Student {student.full_name} has been {status}.")
    return redirect('communityagent_dashboard')


@login_required
def manual_mpesa_donation(request):
    if request.method == 'POST':
        form = ManualMpesaDonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.save()
            messages.success(request, 'Thank you! Your donation details have been submitted. We will verify and contact you if needed.')
            return redirect('donor_donation_history')
    else:
        form = ManualMpesaDonationForm()
    return render(request, 'forms/manual_mpesa_donation.html', {'form': form})

@login_required
def donor_donation_history(request):
    donations = ManualMpesaDonation.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'forms/donor_donation_history.html', {'donations': donations})

@login_required
def update_child_wallet(request):
    # Only allow parents
    role_name = str(request.user.role.name).strip().lower() if request.user.role else None
    if role_name != 'parent':
        messages.error(request, f'Unauthorized access. Your role: {role_name!r}')
        return redirect('homepage')
    # Get children for this parent
    children = Student.objects.filter(parent=request.user)
    if request.method == 'POST':
        form = ManualMpesaDonationForm(request.POST)
        student_id = request.POST.get('student')
        if form.is_valid() and student_id:
            donation = form.save(commit=False)
            donation.user = request.user
            donation.name = request.user.full_name
            donation.save()
            messages.success(request, 'Funds submitted! We will verify and update your child\'s wallet soon.')
            return redirect('view_child_wallet')
    else:
        form = ManualMpesaDonationForm()
    return render(request, 'forms/update_wallet.html', {'form': form, 'children': children, 'user': request.user})

@login_required
def view_child_wallet(request):
    # Only allow parents
    role_name = str(request.user.role.name).strip().lower() if request.user.role else None
    if role_name != 'parent':
        messages.error(request, f'Unauthorized access. Your role: {role_name!r}')
        return redirect('homepage')
    # Get all topups for this parent (across all their children)
    topups = WalletTopUp.objects.filter(parent=request.user).select_related('wallet__student__school').order_by('-submitted_at')
    # Get all wallets for this parent's children
    wallets = ChildWallet.objects.filter(student__parent=request.user).select_related('student__school')
    return render(request, 'forms/view_wallet.html', {'topups': topups, 'wallets': wallets})

def homepage_mpesa_donation(request):
    if request.method == 'POST':
        donor_name = request.POST.get('donor_name') or request.POST.get('donor')
        amount = request.POST.get('amount')
        transaction_code = request.POST.get('transaction_code')
        phone = request.POST.get('phone', '')
        if not (donor_name and amount and transaction_code):
            messages.error(request, 'All fields are required.')
            return redirect('homepage')
        try:
            amount = float(amount)
        except ValueError:
            messages.error(request, 'Invalid amount.')
            return redirect('homepage')
        # Save the donation using ManualMpesaDonation
        ManualMpesaDonation.objects.create(
            name=donor_name,
            amount=amount,
            transaction_code=transaction_code,
            phone=phone,
            verified=False,
        )
        return redirect('homepage_donation_thankyou')
    return redirect('homepage')

def homepage_donation_thankyou(request):
    return render(request, 'forms/donation_thank_you.html')



# View to list donors registered for a specific event
@login_required
def registered_donors(request, event_id=None):
    if event_id:
        event = get_object_or_404(Event, id=event_id)
        event_participations = EventParticipation.objects.filter(event=event).select_related('donor').order_by('-id')
    else:
        event = None
        event_participations = EventParticipation.objects.select_related('donor', 'event').order_by('-id')
    return render(request, 'forms/registered_donors.html', {
        'event': event,
        'event_participations': event_participations
    })

@login_required
def student_management(request):
    # Only allow school admins
    if not request.user.role or request.user.role.name.lower() != 'school admin':
        return redirect('homepage')
    students = Student.objects.select_related('school', 'parent').all().order_by('-id')
    return render(request, 'student_management.html', {'students': students})

@require_POST
@login_required
def verify_student(request, student_id):
    # Only allow school admins
    if not request.user.role or request.user.role.name.lower() != 'school admin':
        return redirect('homepage')
    student = get_object_or_404(Student, id=student_id)
    student.verified = True
    student.save()
    return redirect('student_management')












