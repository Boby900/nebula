from django import forms
from .models import Book

class OrderForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        labels = {

            'title' : 'Title',
            'genre' : 'Genre' ,
            'author' : 'Author Name' ,
            'publishDate' : 'Publish Date' ,
        }

        widgets  ={
            'title' : forms.TextInput(attrs={'placeholder': 'eg. Homo Sapiens'}),
            'genre' : forms.TextInput(attrs={'placeholder': 'eg. Fiction'}),
            'author' : forms.TextInput(attrs={'placeholder': 'eg. Yuval Noah Harrari'}),
            'publishDate' : forms.DateTimeInput(attrs={'placeholder': 'eg. 22/09/2222'}),
        }