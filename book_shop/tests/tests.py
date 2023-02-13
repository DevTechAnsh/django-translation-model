import pytest
from book.forms import BookTranslationForm
from book.models import Book
from django.conf import settings
from django.contrib.auth.models import User


def get_language_code():
    return [language[0] for language in settings.LANGUAGES]


@pytest.mark.django_db
def test_user_create():
    User.objects.create_superuser("john", "lennon@thebeatles.com", "johnpassword")
    assert User.objects.count() == 1
    assert User.objects.get(username="john").is_superuser == True


def test_book_create(db):
    Book.objects.create(
        author_name="David Beazley",
        book_name={
            "en": "Advanced-level programmers",
            "fr": "Programmeurs de niveau avancé",
            "es": "Programadores de nivel avanzado",
        },
    )
    assert Book.objects.count() == 1
    assert (
        Book.objects.get(author_name="David Beazley").book_name.get("en")
        == "Advanced-level programmers"
    )


def test_admin_form_book_create(db):
    kwargs = {
        "author_name": "David Beazley",
        "book_name_en": "Advanced-level programmers",
        "book_name_fr": "Programmeurs de niveau avancé",
        "book_name_es": "Programadores de nivel avanzado",
    }
    form = BookTranslationForm(data=kwargs)
    assert True == form.is_valid()


def test_get_admin_form_book_detail(db):
    book = Book.objects.create(
        author_name="David Beazley",
        book_name={
            "en": "Advanced-level programmers",
            "fr": "Programmeurs de niveau avancé",
            "es": "Programadores de nivel avanzado",
        },
    )
    form = BookTranslationForm(book)
    form.fields.pop("author_name")
    book_name_keys = list(
        map(lambda a: a.replace("book_name_", ""), form.fields.keys())
    )
    assert book_name_keys == get_language_code()


def test_update_admin_form_book_detail(db):
    book = Book.objects.create(
        author_name="David Beazley",
        book_name={
            "en": "Advanced-level programmers",
            "fr": "Programmeurs de niveau avancé",
            "es": "Programadores de nivel avanzado",
        },
    )
    data = {"book_name_ko": "고급 수준의 프로그래머"}
    form = BookTranslationForm(book, data)
    form.fields.pop("author_name")
    book_name_keys = list(
        map(lambda a: a.replace("book_name_", ""), form.fields.keys())
    )
    assert book_name_keys == get_language_code()
