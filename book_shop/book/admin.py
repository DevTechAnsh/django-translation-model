from django.conf import settings
from django.contrib import admin
from django import forms
from .forms import BookTranslationForm
from .models import Book

class BookAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, change=False, **kwargs):
        return BookTranslationForm

    def save_model(self, request, obj, form, change):
        form.cleaned_data.pop('author_name')
        obj.book_name = {key.replace('book_name_', ''): value for key, value in form.cleaned_data.items()}
        obj.save()

admin.site.register(Book, BookAdmin)
