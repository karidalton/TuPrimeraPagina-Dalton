from django import forms
from . import models

class SuscriptorForm(forms.ModelForm):
    class Meta:
        model = models.Suscriptor
        fields = "__all__"


class SedeForm(forms.ModelForm):
    class Meta:
        model = models.Sede
        fields = "__all__"


class SuscriptoPorSedeForm(forms.ModelForm):
    class Meta:
        model = models.SuscriptoPorSede
        fields = "__all__"
        
