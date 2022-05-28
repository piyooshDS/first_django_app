from django.core.exceptions import ValidationError
from django.http import request
from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from business.models import record,product


class compare(forms.ModelForm):
	name=forms.CharField(max_length=15,error_messages={'required': 'Please let us know what to call you!'})
	email=forms.EmailField()
	password=forms.CharField(max_length=10,validators=[RegexValidator(regex="([a-zA-Z0-9]{8})",message=" password length must be 8")])
	contact=forms.CharField(max_length=10)
	want_to=forms.CharField(max_length=10,validators=[RegexValidator()])

	class Meta:
		model=record
		fields=['name','email','password','contact','want_to']

	'''def clean_want_to(self):
		word=self.cleaned_data.get("want_to")
		print(word)
		if word !="sell" or word!="buy":
			raise forms.ValidationError("Please write appropiate word,see example")
		return want_to'''

	def save(self,commit=True):
		user=super(compare,self).save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user


class equal(forms.ModelForm):
	seller=forms.CharField(max_length=15)
	name=forms.CharField(max_length=20)
	price=forms.CharField(max_length=10,validators=[RegexValidator(regex="[0-9]",message="must be integer")])
	details=forms.CharField(max_length=200)

	class Meta:
		model=product
		fields='__all__'