from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Div, Layout

class ReviewForm(forms.Form):
    Email = forms.CharField(required=False,widget=forms.TextInput(attrs={
    'placeholder':'Enter You Email.Not Required'
    }))
    Review =   forms.CharField(required=True,widget=forms.Textarea(attrs={
        'placeholder':'Enter Your review'
    }))
    Ratings = forms.CharField(required=True,widget=forms.TextInput(attrs={
        'placeholder':'Enter Ratings'
    }))
PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('J', 'JazzCash'),
    ('C', 'CashOnDelivery')
)
class SearchForm(forms.Form):
        Search_Criteia = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'placeholder':'Search...'
    }))
class CheckoutForm(forms.Form):
    Shipping_Name = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'placeholder':'Recievers Full Name'
    }))
    Shipping_Country = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'placeholder':'Pakistan'
    }))
    Title = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'placeholder':'Mr.'
    }))
    First_Name = forms.CharField(required=True,widget=forms.TextInput(attrs={
        'placeholder':'First Name'
    }))
    Last_Name = forms.CharField(required=True,widget=forms.TextInput(attrs={
        'placeholder':'Last Name'
    }))
    Shipping_Address = forms.CharField(required=True,widget=forms.TextInput(attrs={
        'placeholder':'Block, Street'
    }))
    Shipping_Address_b = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'placeholder':'City'
    }))
    Zip = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'placeholder':'Zip'
    }))
    Phone = forms.CharField(required=True,widget=forms.TextInput(attrs={
        'placeholder':'Phone'
    }))
    Alt_Phone = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'placeholder':'Phone-2'
    }))
    Same_Billing_Address = forms.BooleanField(required=False)
    Shipping_Note=forms.CharField(required=False,widget=forms.TextInput(attrs={

        'placeholder':'Important Details.',
        'rows':'16'
    }))
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect(),choices=PAYMENT_CHOICES)