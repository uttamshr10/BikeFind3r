from listings import models
from django import forms

class FormList(forms.ModelForm):
    class Meta:
        model = models.Listings
        fields = ['title', 'condition', 'product_type', 'sale_type', 'price', 'main_photo', 'photo_1',
'photo_2', 'city', 'state', 'zipcode', 'contact_email', 'list_date']