from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 4)]
PRODUCT_QUANTITY_CHOICES_1 = [(1, '1'), (2, '2'), (4, '4'), (8, '8')]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    number = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES_1, coerce=int, label='Количество кусков')