# -*- coding:utf-8 -*-

from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=300)
    skypeid = forms.CharField(label="Ваш skypeid", max_length=200)
    time = forms.CharField(label="Удобное время для связи", max_length=4096)
    captcha = CaptchaField()
