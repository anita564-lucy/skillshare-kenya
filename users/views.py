from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, ProviderProfile, SeekerProfile
from .forms import ProfileForm


@login_required
def profile(request):
    user = request.user
    if user.type == User.Types.PROVIDER:
        try:
            profile = user.provider_profile
        except ProviderProfile.DoesNotExist:
            profile = ProviderProfile.objects.create(user=user)
    else:
        try:
            profile = user.seeker_profile
        except SeekerProfile.DoesNotExist:
            profile = SeekerProfile.objects.create(user=user)
    return render(request, "users/profile.html", {"profile": profile})


@login_required
def profile_edit(request):
    user = request.user
    if user.type == User.Types.PROVIDER:
        try:
            profile = user.provider_profile
        except ProviderProfile.DoesNotExist:
            profile = ProviderProfile.objects.create(user=user)
        form_class = ProfileForm
    else:
        try:
            profile = user.seeker_profile
        except SeekerProfile.DoesNotExist:
            profile = SeekerProfile.objects.create(user=user)
        form_class = ProfileForm

    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("users:profile")
    else:
        form = form_class(instance=profile)
    return render(request, "users/profile_edit.html", {"form": form})