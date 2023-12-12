from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, EmailInput, PasswordInput, CharField, EmailField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class createApplication(ModelForm):
    class Meta:
        model = Team
        # 9 fields
        fields = ['name', 'logo', 'tournament', 'country', 'countOfPlayers', 'coach', 'email', 'pnumber', 'info']

        labels = {
            'name': '',
            'logo': '',
            'tournament': '',
            'country': '',
            'countOfPlayers': '',
            'coach': '',
            'email': '',
            'pnumber': '',
            'info': ''
        }

        widgets = {
            'name': TextInput(attrs={'class': 'form-application', 'placeholder': 'Название(в названии укажите категорию)'}),
            'country': TextInput(attrs={'class': 'form-application', 'placeholder': 'Страна'}),
            'countOfPlayers': TextInput(attrs={'class': 'form-application', 'placeholder': 'Турнир'}),
            'coach': TextInput( attrs={'class': 'form-application', 'placeholder': 'Тренер команды'}),
            'email': EmailInput(attrs={'class': 'form-application', 'placeholder': 'E-mail'}),
            'pnumber': PhoneNumberPrefixWidget(attrs={'class': 'form-application', 'placeholder': 'Номер телефона'}),
            'info': Textarea(attrs={'class': 'form-application', 'placeholder': 'Дополнительная информация'})

        }

class sendContact(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'topic', 'message']

        labels = {
            'name': '',
            'email': '',
            'topic': '',
            'message': '',
            'phone_number': ''
        }

        widgets = {
            'name': TextInput(
                attrs={'class': 'contact-form-fp', 'id': 'contact-fp-form-name', 'placeholder': 'Ваше имя'}),
            'email': EmailInput(
                attrs={'class': 'contact-form-fp', 'id': 'contact-fp-form-email', 'placeholder': 'Email'}),
            'topic': TextInput(
                attrs={'class': 'contact-form-fp', 'id': 'contact-fp-form-topic', 'placeholder': 'Тема'}),
            'phone_number': TextInput(
                attrs={'class': 'contact-form-fp', 'id': 'contact-fp-form-phone_number', 'placeholder': 'Номер телефона'}),
            'message': Textarea(
                attrs={'class': 'contact-form-fp', 'id': 'contact-fp-form-message', 'placeholder': 'Сообщение'})

        }