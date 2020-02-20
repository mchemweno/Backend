from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id) + ". " + self.category_name


class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=25)
    searches = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + ". " + self.service_name


class UserType(models.Model):
    user_type = models.CharField(max_length=25)

    def __str__(self):
        return str(self.id) + ". " + self.user_type


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=25, unique=True)
    bio = models.TextField(max_length=500, null=True)
    phone = models.CharField(null=True, max_length=25)
    profile_picture = ProcessedImageField(upload_to='profile_pictures/%y/%m/%d', processors=[ResizeToFill(300, 300)],
                                          format='PNG')
    average_rating = models.IntegerField(default=0)
    # user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    # service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    REQUIRED_FIELDS = ['username', 'profile_picture', 'phone', 'first_name', 'last_name', 'bio']

    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class Reviews(models.Model):
    review = models.CharField(max_length=500)
    rating = models.IntegerField()
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewee = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.reviewee + " ." + self.review + " " + self.reviewer
