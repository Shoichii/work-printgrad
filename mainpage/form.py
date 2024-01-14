from django import forms
from django.forms.models import ModelForm
from .models import Candidate, Citizenships
import datetime
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# class Calculator(ModelForm):
#     city = forms.ModelChoiceField(queryset=Cities.objects.all(),
#                                 widget=forms.Select(attrs={'class': 'calc-city'}))
#     vacancy = forms.ModelChoiceField(queryset=Vacancies.objects.all(),
#                                     widget=forms.Select(attrs={'class': 'calc-vacancy'}))

#     class Meta:
#         model = CitiesVacancies
#         fields = ['city', 'vacancy']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['city'].label = False
#         self.fields['vacancy'].label = False
#         self.fields['city'].empty_label = 'Выберите город'
#         self.fields['vacancy'].empty_label = 'Выберите вакансию'


def validate_phone_number(value):
    pattern = re.compile(r'^\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}$')
    if not pattern.match(value):
        raise ValidationError(
            _('Invalid phone number format.'),
            params={'value': value},
        )


class FillForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Введите имя на русском языке'}))
    # surname = forms.CharField(widget=forms.TextInput(
    #     attrs={'placeholder': 'Введите отчество на русском языке(при наличии)'}),
    #     required=False)
    # last_name = forms.CharField(widget=forms.TextInput(
    #     attrs={'placeholder': 'Введите фамилию на русском языке'}))
    birthday = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'ДД.ММ.ГГГГ'}))
    citizenship = forms.ModelChoiceField(
        queryset=Citizenships.objects.all(), widget=forms.Select(), required=False)
    custom_citizenship = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Введите своё гражданство'}), required=False)
    # city = forms.ModelChoiceField(queryset=Cities.objects.all(),
    #                             widget=forms.Select(attrs={'class': 'fill-form-city'}))
    # vacancy = forms.ModelChoiceField(queryset=Vacancies.objects.all(),
    #                                 widget=forms.Select(attrs={'class': 'fill-form-vacancy'}))
    phone = forms.CharField(validators=[validate_phone_number], widget=forms.TextInput(attrs={'placeholder': '___-__-__',
                                                            'value': '+7 ',
                                                            'pattern': r'\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}',
                                                            'title': 'Пожалуйста, введите номер телефона',
                                                            'data-toggle':"tooltip",
                                                            'data-placement':"right"
                                                            }))
    resume_file = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'fill-form-file'}), required=False)
    resume_link = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'ссылка на резюме'}), required=False,)
    # sources = forms.ModelChoiceField(queryset=Sources.objects.all(), 
    #                                 widget=forms.RadioSelect(attrs={'class': 'fill-form-source'}))

    class Meta:
        model = Candidate
        fields = ['first_name','birthday', 'citizenship', 'custom_citizenship','phone', 'resume_file',
                'resume_link']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['city'].label = False
        # self.fields['vacancy'].label = False
        # self.fields['city'].empty_label = 'Выберите город'
        # self.fields['vacancy'].empty_label = 'Выберите вакансию'
        self.fields['citizenship'].label = False
        self.fields['citizenship'].empty_label = 'Выберите гражданство'

    def clean_birthday(self):
        birthday = self.cleaned_data['birthday']
        try:
            birthday = datetime.datetime.strptime(birthday, '%d.%m.%Y').strftime('%Y-%m-%d')
        except ValueError:
            raise forms.ValidationError('Неверный формат даты')
        return birthday
    