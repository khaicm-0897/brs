from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Book, BookRequestBuy


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name',
                  'description',
                  'image',
                  'book_category',
                  'author',
                  'paperback',
                  'language',
                  'publisher',
                  'price']


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name',
                  'description',
                  'image',
                  'book_category',
                  'author',
                  'paperback',
                  'language',
                  'publisher',
                  'price']


class BookMarkReadForm(forms.Form):
    page_reading = forms.IntegerField(min_value=1)


class BookFavoriteForm(forms.Form):
    is_favorite = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])


class BookRequestBuyForm(forms.ModelForm):
    class Meta:
        model = BookRequestBuy
        fields = ['name', 'book_url', 'book_category', 'price']


class BookRequestBuyUpdateForm(forms.Form):
    status = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])


class BookReviewCreateForm(forms.Form):
    message = forms.CharField(max_length=512)


class BookRatingCreateForm(forms.Form):
    rating = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


class SearchBookForm(forms.Form):
    q = forms.CharField(max_length=128)
