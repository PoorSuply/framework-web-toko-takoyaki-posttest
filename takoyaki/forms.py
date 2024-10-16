from django import forms
from .models import TakoyakiMenu

class TakoyakiMenuForm(forms.ModelForm):
    class Meta:
        model = TakoyakiMenu
        fields = ['item_name', 'price', 'description', 'is_available']
