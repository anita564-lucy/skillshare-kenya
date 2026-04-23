from django.urls import path
from . import views

app_name = "skills"

urlpatterns = [
    path("", views.skills_list, name="skills_list"),
    path("<int:pk>/", views.skill_detail, name="skill_detail"),
    path("create/", views.skill_create, name="skill_create"),
    path("<int:pk>/edit/", views.skill_edit, name="skill_edit"),
    path("<int:pk>/delete/", views.skill_delete, name="skill_delete"),
]