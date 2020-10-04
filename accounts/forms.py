from django.forms import ModelForm
from .models import Order, Customer

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields['name'].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields['phone'].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields['email'].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields['profile_pic'].widget.attrs.update({
                'class': 'form-control'
            })


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



