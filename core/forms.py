from django import forms
from .models import Role, User, School, Student, Donation, FeedingReport, Feedback, Event, EventParticipation, Attendance

# Form to create or update a Role instance
class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name']
        widgets = {
            # Bootstrap styling and placeholder for user-friendly input
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role name'}),
        }

# Form to create or update a User instance : Handles validation and form rendering
class UserForm(forms.ModelForm):
            # Use PasswordInput widget to mask password input in forms
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        role = forms.ModelChoiceField(
        queryset=Role.objects.all(),
        empty_label="Select Role",
        widget=forms.Select(attrs={'class': 'form-control'})
    )


        class Meta:
         model = User
         fields = [ 'full_name', 'email', 'password','role']
         widgets = {
            #'role': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for selecting role
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'})
        }

# Form to create or update School details
class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name', 'location', 'email', 'phone_number']
        widgets = {
            'school_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'School name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
        }

# Form to create or update Student information
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'grade', 'school', 'parent']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student full name'}),
            'grade': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),  # Grade must be positive integer
            'school': forms.Select(attrs={'class': 'form-control'}),               # Select school from existing entries
            'parent': forms.Select(attrs={'class': 'form-control'}),               # Select parent user
        }

# Form to record a Donation made by a donor to a school
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donor', 'amount', 'school']
        widgets = {
            'donor': forms.Select(attrs={'class': 'form-control'}),               # Donor user selection
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),  # Positive decimal amount
            'school': forms.Select(attrs={'class': 'form-control'}),              # Recipient school selection
        }

# Form to submit Feeding Reports for schools
class FeedingReportForm(forms.ModelForm):
    class Meta:
        model = FeedingReport
        fields = ['user', 'school', 'report_date', 'meals_received', 'meals_served', 'comments']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),                # Reporter (user)
            'school': forms.TextInput(attrs={'class': 'form-control'}),              # School reported on
            'report_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Date picker input
            'meals_received': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),  # Non-negative integer
            'meals_served': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),    # Non-negative integer
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),          # Optional comments
        }

# Form to collect user Feedback messages
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['user', 'message']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),                # Feedback author
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your feedback'}),  # Feedback text
        }

# Form to create or update Events related to the program
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date', 'school', 'created_by']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'school': forms.Select(attrs={'class': 'form-control'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # Show only users whose role is 'Community Agent'
        self.fields['created_by'].queryset = User.objects.filter(role__name='Community Agent')
        print(self.fields['created_by'].queryset)



# Form to manage participation of donors in events
class EventParticipationForm(forms.ModelForm):
    class Meta:
        model = EventParticipation
        fields = ['event', 'donor']
        widgets = {
            'event': forms.Select(attrs={'class': 'form-control'}),               # Event selection
            'donor': forms.Select(attrs={'class': 'form-control'}),               # Donor user selection
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #  donor filtering 
        self.fields['donor'].queryset = User.objects.filter(role__name='Donor')

# Form to record student Attendance for a given date
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'attendance', 'attendance_date']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),             # Student selection
            'attendance': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Present or absent checkbox
            'attendance_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Date picker
        }




