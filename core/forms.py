from django import forms
from .models import Project, Skill, Contact


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technology_used', 'github_link', 'live_link']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Project title'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Short description'}),
            'technology_used': forms.TextInput(attrs={'placeholder': 'Django, PostgreSQL, React'}),
            'github_link': forms.URLInput(attrs={'placeholder': 'https://github.com/...'}),
            'live_link': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name', 'skill_level']
        widgets = {
            'skill_name': forms.TextInput(attrs={'placeholder': 'e.g. Python'}),
            'skill_level': forms.NumberInput(attrs={'min': 1, 'max': 100, 'placeholder': '85'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Your message...'}),
        }