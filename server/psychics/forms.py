from django import forms


class UserNumberForm(forms.Form):
    user_number = forms.IntegerField(
        label='Введите число, которое вы загадали',
        min_value=10,
        max_value=99,
        error_messages={
            'required': 'This field is required.',
            'min_value': 'The number must be between 10 and 99.',
            'max_value': 'The number must be between 10 and 99.',
        }
    )
