from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import AddBook , EditBook

#add book
class AddBookForm(forms.ModelForm):
    
    class Meta :
        model = AddBook
        fields = ['book_name','book_image', 'book_price']

class EditBookForm(forms.ModelForm):
    book_name = forms.CharField(max_length=255)
    book_image = forms.ImageField(required=False) 
    book_price = forms.DecimalField(max_digits=10,decimal_places=2)
       
    class Meta :
        model = EditBook
        fields = ['book_name','book_image', 'book_price']
