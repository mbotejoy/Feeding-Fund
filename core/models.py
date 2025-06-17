from django.db import models

# Represents different user roles (e.g., donor, admin, parent)
class Role(models.Model):
    role = models.CharField(max_length=50)  # Name of the role

    def _str_(self):
        return self.role

# Custom user model 
class User(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)  # User's role
    full_name = models.CharField(max_length=255)              # Full name of the user
    email = models.EmailField(unique=True)                    # Unique email address
    password = models.CharField(max_length=128)               # Password (should be hashed)
    created_at = models.DateTimeField(auto_now_add=True)      # Timestamp of user creation

    def _str_(self):
        return self.full_name

# Represents a school participating in the program
class School(models.Model):
    school_name = models.CharField(max_length=255)            # Name of the school
    location = models.CharField(max_length=255)               # Physical location
    email = models.EmailField()                               # Contact email
    phone_number = models.CharField(max_length=20)            # Contact phone number
    created_at = models.DateTimeField(auto_now_add=True)      # Timestamp of school entry

    def _str_(self):
        return self.school_name

# Represents a student enrolled in a school
class Student(models.Model):
    full_name = models.CharField(max_length=100)              # Student's full name
    grade = models.IntegerField()                             # Grade or class
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Associated school
    parent = models.ForeignKey(User, on_delete=models.CASCADE)    # Parent or guardian (User)

    def _str_(self):
        return self.full_name

# Records a donation made by a user to a school
class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)     # Donor (User)
    amount = models.DecimalField(max_digits=10, decimal_places=2) # Donation amount
    date = models.DateTimeField(auto_now_add=True)                # Date and time of donation
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Recipient school

# Report on the feeding program at a school
class FeedingReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)      # User submitting the report
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # School being reported on
    report_date = models.DateField()                              # Date of the report
    meals_received = models.IntegerField()                        # Number of meals received
    meals_served = models.IntegerField()                          # Number of meals served
    comments = models.TextField(blank=True)                       # Additional comments (optional)

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
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Associated school
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)# User who created the event
    created_at = models.DateTimeField(auto_now_add=True)          # Timestamp of event creation

    def _str_(self):
        return self.title

# Tracks which users (donors) participate in which events
class EventParticipation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)    # Event participated in
    donor = models.ForeignKey(User, on_delete=models.CASCADE)     # Donor participating

# Records student attendance for a particular date
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE) # Student
    attendance = models.BooleanField()                             # Present (True) or absent (False)
    attendance_date = models.DateField()                           # Date of attendance