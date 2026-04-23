from django import forms
from .models import Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["title", "description", "category", "location", "price", "image", "is_available"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "e.g. Python Tutoring"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Describe your skill..."}),
            "location": forms.TextInput(attrs={"placeholder": "e.g. Nairobi, Mombasa"}),
            "price": forms.NumberInput(attrs={"placeholder": "Price in KES"}),
        }