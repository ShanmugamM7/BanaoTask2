from django.contrib.auth.models import AbstractUser,User
from django.db import models
from django.conf import settings

class UserDetails(AbstractUser):
    USER_TYPE_CHOICES = (
        ('P', 'Patient'),
        ('D', 'Doctor'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='Not Mentioned')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    address_line1 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

class BlogPost(models.Model):
    # Define category choices
    CATEGORY_CHOICES = (
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid19'),
        ('Immunization', 'Immunization'),
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, default='')
    summary = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    draft = models.BooleanField(default=False)

    

    def __str__(self):
        return self.title