from django import forms
from django.conf import settings

from .models import Book

class BookTranslationForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ["book_name"]

    def __init__(self, *args, **kwargs):
        super ().__init__ (*args, **kwargs)
        for key,val in settings.LANGUAGES:
            self.base_fields[f'book_name_{key}'] = forms.CharField(required=True, label=f'Book Name ({key})')
            if hasattr(self, "instance"):
                self.initial.update({f"book_name_{k}": v for k, v in self.instance.book_name.items ()})