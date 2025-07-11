from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.conf import settings


# Represents different user roles (e.g., donor, admin, parent)
class Role(models.Model):
    ROLE_CHOICES = [
        ('Donor', 'Donor'),
        ('Parent', 'Parent'),
        ('School Admin', 'School Admin'),
        ('Community Agent', 'Community Agent'),
    ]

    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name  # shows human-readable label
    

# Custom manager for User
#resolves the Django admin login error and allow you to manage users through the admin interface.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)

# Custom user model 
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('Donor', 'Donor'),
        ('Parent', 'Parent'),
        ('School Admin', 'School Admin'),
        ('Community Agent', 'Community Agent'),
    )
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True, blank=True, help_text='Assign a school to this user (for school admins)')
    full_name = models.CharField(max_length=255)              # Full name of the user
    email = models.EmailField(unique=True)                    # Unique email address
    password = models.CharField(max_length=128)               # Password (should be hashed)
    created_at = models.DateTimeField(auto_now_add=True)      # Timestamp of user creation

    is_active = models.BooleanField(default=True)               #Determines if user account is active
    is_staff = models.BooleanField(default=False)               #Determines if user can access the Django admin site
    last_login = models.DateTimeField(null=True, blank=True)    #Stores the timestamp of the user's last successful login.
    is_verified = models.BooleanField(default=False)             # Determines if the user's email is verified

    USERNAME_FIELD = 'email'  # Use email for login

    objects = UserManager()

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
    is_active = models.BooleanField(default=True)  # Add this field to allow activation/deactivation
    verified = models.BooleanField(default=False)  # School admin must verify student

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
    event_time = models.TimeField(null=True, blank=True)          # Time of the event
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

class ManualMpesaDonation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='manual_donations', null=True, blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_code = models.CharField(max_length=20, unique=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.transaction_code}"

class ChildWallet(models.Model):
    student = models.OneToOneField('Student', on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.full_name} Wallet: {self.balance} KES"

class WalletTopUp(models.Model):
    wallet = models.ForeignKey(ChildWallet, on_delete=models.CASCADE, related_name='topups')
    parent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_code = models.CharField(max_length=20, unique=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.wallet.student.full_name} TopUp: {self.amount} KES ({self.transaction_code})"