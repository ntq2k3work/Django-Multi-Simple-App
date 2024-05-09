from django import forms 
from captcha.fields import CaptchaField,CaptchaAnswerInput
from django_recaptcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox 
class ContactForm(forms.Form): 
    email = forms.EmailField() 
    feedback = forms.CharField(widget=forms.Textarea) 
    captcha  =  ReCaptchaField()