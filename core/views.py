from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required          #Ensures the user is authenticated
from django.shortcuts import render, redirect, get_object_or_404
from core.forms import (DonationForm, FeedingReportForm, EventForm, EventParticipationForm,UserForm, SchoolForm, FeedingReportForm,StudentForm,AttendanceForm,FeedbackForm)
from core.models import (Donation, FeedingReport, Event, User, School,Role,Student,Attendance)



#View of the User Registration page
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
    

#login view    
def login(request):
    if request.method == 'POST':
        # Get the submitted values from the login form
        email = request.POST.get('username')  # full name field used as username
        password = request.POST.get('password')   # Password field

        try:
            # Try to retrieve the user from the database using full_name
            user = User.objects.get(email=email)

            # Check if the entered password matches the user's stored hashed password
            if check_password(password, user.password):
                # If password is correct, log in the user manually
                auth_login(request, user)

                # Redirect the user to the appropriate dashboard based on their role
                role = user.role.name.lower()  # Convert role to lowercase for easier comparison

                if role == 'donor':
                    return redirect('donor_dashboard')
                elif role == 'school admin':
                    return redirect('school_admin')
                elif role == 'community agent':
                    return redirect('communityagent_dashboard')
                elif role == 'parents':
                    return redirect('parent')
                else:
                    # If role is not matched, go to homepage
                    return redirect('homepage')

            else:
                # If the password is incorrect, show an error message and redirect to homepage
                messages.error(request, 'Invalid password.')
                return redirect('homepage')

        except User.DoesNotExist:
            # If no user with that full name exists, show an error and redirect to homepage
            messages.error(request, 'User with that name does not exist.')
            return redirect('homepage')

    # If GET request, show the login form
    return render(request, 'forms/login.html')
    
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


# Handle event participation form
def join_an_event(request):
    if request.method == 'POST':
        form = EventParticipationForm(request.POST)
        if form.is_valid():
            form.save()  # Save event participation
            messages.success(request, "You have successfully joined the event!")
            return redirect('donor_dashboard')  # Redirect to dashboard after submission
    else:
        form = EventParticipationForm()  # Display blank form for GET request

    return render(request, 'forms/event_participation.html', {'form': form})  # Render the form template

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
    return render(request, 'donor_dashboard.html')  

# Show the community_agent dashboard
@login_required
def communityagent_dashboard(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'communityagent_dashboard.html', {
        'attendance_records': attendance_records
    })

# Show the school admin dashboard
@login_required
def school_admin(request):
    return render(request, 'teacher.html')

# Show the parent dashboard
@login_required
def parent(request):
    return render(request, 'parent.html')


#Takes to home page
def homepage(request):
    return render(request, 'forms/nourished.html')

#About Us Page
def about_us(request):
    return render(request, 'forms/nourished.html')

#Impact Page
def impact(request):
    return render(request, 'forms/nourished.html')



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

    # Optional confirmation page (or delete instantly if you prefer)
    return render(request, 'forms/confirm_delete.html', {'record': record})













