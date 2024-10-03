# store/forms.py
from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
