from django import forms

from .models import Categories


class SearchForm(forms.Form):
    query = forms.CharField(
        label='Поиск', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Поиск'})
    )
    category = forms.ChoiceField(label='Категория', choices=[('all', 'Все')] + list(Categories.objects.values_list('slug', 'name')), required=False)
        