from django import forms
from core.models import *
from django.contrib.auth.models import User

class ProductReviewForm(forms.ModelForm):
    review=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Write Review'}))
    
    class Meta:
        model=Product_Review
        fields=['review','rating']



