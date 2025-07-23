from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class SearchForm(forms.Form):
    q = forms.CharField(max_length=100)

 
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  
        fields = ['title', 'author', 'published_date']  