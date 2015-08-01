from django import forms
from questionario.models import Resposta, Questionario

class RespostaForm(forms.ModelForm):
	class Meta:
		model = Resposta
		exclude = ['post']

class QuestionarioForm(forms.ModelForm):
	class Meta:
		model = Questionario
		exclude = ['post']