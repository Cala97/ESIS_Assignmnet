from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True, help_text="Date of Birth")
    photo = models.ImageField(
        null=True,
        blank=True,
        upload_to='profile_photos/',
        help_text="Profile Photo",
    )

    def __str__(self):
        return f"Profile for {self.user.username}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
