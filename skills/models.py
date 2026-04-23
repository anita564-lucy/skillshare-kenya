from django.db import models
from users.models import User


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("tech", "Technology"),
        ("design", "Design"),
        ("education", "Education"),
        ("business", "Business"),
        ("music", "Music & Arts"),
        ("health", "Health & Fitness"),
        ("other", "Other"),
    ]

    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills")
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in KES")
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="skills/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.provider.email}"

    class Meta:
        ordering = ["-created_at"]