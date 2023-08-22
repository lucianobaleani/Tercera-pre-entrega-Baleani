from django import forms


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=70)
    role = forms.CharField(max_length=70)
    nationality = forms.CharField(max_length=70)


class EditorialForm(forms.Form):
    name = forms.CharField(max_length=70)
    country = forms.CharField(max_length=70)
    state = forms.CharField(max_length=70)


class ComicForm(forms.Form):
    name = forms.CharField(max_length=70)
    published_year = forms.IntegerField()
    editorial = forms.CharField(max_length=70)
