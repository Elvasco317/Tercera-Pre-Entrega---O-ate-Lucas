from django import forms

class busca_cursoform(forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()