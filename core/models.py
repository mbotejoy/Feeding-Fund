from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


# Represents different user roles (e.g., donor, admin, parent)
class Role(models.Model):
    ROLE_CHOICES = [
        ('Donor', 'Donor'),
        ('Parent', 'Parent'),
        ('School Admin', 'School Admin'),
        ('Community Agent', 'Community Agent'),
    ]

    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()  # shows human-readable label
    

# Custom user model 
class User(AbstractBaseUser, PermissionsMixin):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)  # User's role
    full_name = models.CharField(max_length=255)              # Full name of the user
    email = models.EmailField(unique=True)                    # Unique email address
    password = models.CharField(max_length=128)               # Password (should be hashed)
    created_at = models.DateTimeField(auto_now_add=True)      # Timestamp of user creation

    is_active = models.BooleanField(default=True)               #Determines if user account is active
    is_staff = models.BooleanField(default=False)               #Determines if user can access the Django admin site
    last_login = models.DateTimeField(null=True, blank=True)    #Stores the timestamp of the user's last successful login.

    USERNAME_FIELD = 'email'  # Use email for login

    def __str__(self):
     return self.full_name

# Represents a school participating in the program
class School(models.Model):
    school_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.school_name 

# Represents a student enrolled in a school
class Student(models.Model):
    full_name = models.CharField(max_length=100)              # Student's full name
    grade = models.IntegerField()                             # Grade or class
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Associated school
    parent = models.ForeignKey(User, on_delete=models.CASCADE)    # Parent or guardian (User)


    def __str__(self):
     return self.full_name

# Records a donation made by a user to a school
class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)     # Donor (User)
    amount = models.DecimalField(max_digits=10, decimal_places=2) # Donation amount
    date = models.DateTimeField(auto_now_add=True)                # Date and time of donation
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Recipient school

# Report on the feeding program at a school
class FeedingReport(models.Model):
    user = models.CharField(max_length=255)      # User submitting the report
    school = models.CharField(max_length=255)  # School being reported on
    report_date = models.DateField()                              # Date of the report
    meals_received = models.IntegerField()                        # Number of meals received
    meals_served = models.IntegerField()                          # Number of meals served
    comments = models.TextField(blank=True)                       # Additional comments (optional)
    def __str__(self):
        return f"Report for {self.school} on {self.report_date}"

# User feedback about the system or program
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)      # User giving feedback
    message = models.TextField()                                  # Feedback message
    created_at = models.DateTimeField(auto_now_add=True)          # Timestamp of feedback

# Represents an event related to the program (e.g., fundraiser, outreach)
class Event(models.Model):
    title = models.CharField(max_length=255)                      # Event title
    description = models.TextField()                              # Event description
    event_date = models.DateField()                               # Date of the event
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Associated school;This tells Django: each event is linked to a single school.
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)# User who created the event
    created_at = models.DateTimeField(auto_now_add=True)          # Timestamp of event creation

    def __str__(self):
        return self.title

# Tracks which users (donors) participate in which events
class EventParticipation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)    # Event participated in
    donor = models.ForeignKey(User, on_delete=models.CASCADE)     # Donor participating


# Records student attendance for a particular date
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE) # Student
    attendance = models.CharField(max_length=255)                             # Present (True) or absent (False)
    attendance_date = models.DateField()                           # Date of attendance

    def __str__(self):
     return f"{self.student.full_name} - {self.attendance_date}"