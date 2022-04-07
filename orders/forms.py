from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', max_length=100)
    last_name = forms.CharField(label='Фамилия', max_length=100)
    email = forms.EmailField(label='E-mail')
    address = forms.CharField(label='Адрес', max_length=100)
    postal_code = forms.CharField(label='Почтовый адрес', max_length=100)
    city = forms.CharField(label='Город', max_length=100)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']