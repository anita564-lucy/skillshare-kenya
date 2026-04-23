from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Skill
from .forms import SkillForm


def skills_list(request):
    skills = Skill.objects.filter(is_available=True)
    category = request.GET.get("category")
    if category:
        skills = skills.filter(category=category)
    return render(request, "skills/skills_list.html", {"skills": skills, "category": category})


def skill_detail(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    return render(request, "skills/skill_detail.html", {"skill": skill})


@login_required
def skill_create(request):
    if request.method == "POST":
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.provider = request.user
            skill.save()
            messages.success(request, "Skill listed successfully!")
            return redirect("skills:skills_list")
    else:
        form = SkillForm()
    return render(request, "skills/skill_form.html", {"form": form})


@login_required
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk, provider=request.user)
    if request.method == "POST":
        form = SkillForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill updated successfully!")
            return redirect("skills:skills_list")
    else:
        form = SkillForm(instance=skill)
    return render(request, "skills/skill_form.html", {"form": form})


@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk, provider=request.user)
    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill deleted successfully!")
        return redirect("skills:skills_list")
    return render(request, "skills/skill_confirm_delete.html", {"skill": skill})