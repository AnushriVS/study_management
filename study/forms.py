from django import forms
from .models import Study

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['study_name', 'study_phase', 'sponsor_name', 'study_description']
        labels = {
            'study_name': 'Study Name',
            'study_phase': 'Study Phase',
            'sponsor_name': 'Sponsor Name',
            'study_description': 'Study Description',
        }
        widgets = {
            'study_name': forms.TextInput(attrs={'class': 'form-control'}),
            'study_phase': forms.Select(attrs={'class': 'form-control'}),
            'sponsor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'study_description': forms.Textarea(attrs={'class': 'form-control','style': 'height: 100px; width: 600px;'
}),
        }
