from django import forms
from .models import Role, User, School, Student, Donation, FeedingReport, Feedback, Event, EventParticipation, Attendance, ManualMpesaDonation
from datetime import date

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
    school = forms.ModelChoiceField(queryset=School.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
     model = User
     fields = ['full_name', 'email', 'password', 'school']  # Add 'school' to the form
     widgets = {
        #'role': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for selecting role
        'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        'password' : forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'})
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show the school field if the user is being registered as a school admin
        if not self.initial.get('is_school_admin', False):
            self.fields['school'].widget = forms.HiddenInput()

    def save(self, commit=True):
        user = super().save(commit=False)
        # If the user is a school admin, save the school
        if self.cleaned_data.get('school'):
            user.school = self.cleaned_data['school']
        if commit:
            user.save()
        return user

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
            'parent': forms.HiddenInput(),  # Hide parent field
        }

    def __init__(self, *args, parent=None, **kwargs):
        super().__init__(*args, **kwargs)
        if parent is not None:
            self.fields['parent'].initial = parent.id

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.fields['parent'].initial:
            instance.parent_id = self.fields['parent'].initial
        if commit:
            instance.save()
        return instance

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

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user and user.role and user.role.name.lower() == 'school admin':
            self.fields.pop('school')

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
        fields = ['title', 'description', 'event_date', 'school']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min': date.today().isoformat()}),
            'school': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event_date'].widget.attrs['min'] = date.today().isoformat()
        if user and user.role and user.role.name.lower() == 'school admin':
            self.fields.pop('school')
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        if hasattr(self, 'user') and self.user:
            instance.created_by = self.user
        if commit:
            instance.save()
        return instance

# Form to manage participation of donors in events
class EventParticipationForm(forms.ModelForm):
    class Meta:
        model = EventParticipation
        fields = ['event']  # Only show event selection to the donor
        widgets = {
            'event': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally, filter events if needed
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.donor = self.user
        if commit:
            instance.save()
        return instance

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

# Form to handle manual Mpesa donations
class ManualMpesaDonationForm(forms.ModelForm):
    class Meta:
        model = ManualMpesaDonation
        fields = ['name', 'phone', 'amount', 'transaction_code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'transaction_code': forms.TextInput(attrs={'class': 'form-control'}),
        }




