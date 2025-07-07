from django import forms
from .models_manual_mpesa import ManualMpesaDonation

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
