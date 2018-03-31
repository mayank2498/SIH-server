from django.contrib.auth.models import User
from django import forms
from .models import Farmer,answer,post_question
from django.forms import Textarea,ModelForm 


class farmer_signup(forms.ModelForm):
	class Meta:
		model=Farmer
		fields=('name','address','aadhar','mobile')


class discuss_form(forms.ModelForm):
	ask = forms.CharField(
	max_length=10000,
	widget=forms.Textarea(),
	help_text='Write here your question!'
	)
	def __init__(self, *args, **kwargs):          
		super(discuss_form, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['placeholder'] = u'Write your name'
		self.fields['ask'].widget.attrs['placeholder'] = u'Write your question'
	class Meta:
		model=post_question
		fields=('name','ask')

class comment_form(forms.ModelForm):
	def __init__(self, *args, **kwargs):          
		super(comment_form, self).__init__(*args, **kwargs)
		self.fields['comment'].widget.attrs['placeholder'] = u'Write your comments'
	class Meta:
		model = answer
		fields = ['user_name', 'comment']
		widgets = {
    	'comment': Textarea(attrs={'cols': 45, 'rows': 20,},),
		}

		
