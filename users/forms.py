from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm
from .models import User, ProviderProfile, SeekerProfile


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ("email",)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProviderProfile
        fields = ["profile_image", "bio", "location", "phone", "skill_category"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4, "placeholder": "Tell us about yourself..."}),
            "location": forms.TextInput(attrs={"placeholder": "e.g. Nairobi"}),
            "phone": forms.TextInput(attrs={"placeholder": "e.g. 0712345678"}),
            "skill_category": forms.TextInput(attrs={"placeholder": "e.g. Web Development"}),
        }


class SeekerProfileForm(forms.ModelForm):
    class Meta:
        model = SeekerProfile
        fields = ["profile_image", "bio", "location", "phone"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4, "placeholder": "Tell us about yourself..."}),
            "location": forms.TextInput(attrs={"placeholder": "e.g. Nairobi"}),
            "phone": forms.TextInput(attrs={"placeholder": "e.g. 0712345678"}),
        }