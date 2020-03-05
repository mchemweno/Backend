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
    email = models.EmailField(verbose_name='email', max_length=40, unique=True)
    bio = models.TextField(max_length=500, null=True)
    company = models.CharField(max_length=25, blank=True)
    phone = models.IntegerField(null=True)
    profile_picture = ProcessedImageField(upload_to='profile_pictures/%y/%m/%d',
                                          format='PNG', blank=True, null=True)
    average_rating = models.IntegerField(default=0)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, default=1)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=1)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'profile_picture', 'phone', 'bio', 'company', 'user_type',
                       'service',
                       'average_rating']

    USERNAME_FIELD = 'email'


def get_username(self):
    return self.email


class Review(models.Model):
    review = models.CharField(max_length=500)
    rating = models.IntegerField(default=0)
    reviewee = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewer = models.EmailField(max_length=40)
    reviewer_fname = models.CharField(max_length=10, blank=True)
    reviewer_lname = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.reviewee.email + " ." + str(self.rating) + " "
        self.review


class Report(models.Model):
    complainant_email = models.EmailField(max_length=40)
    complainant_fname = models.CharField(max_length=10)
    complainant_lname = models.CharField(max_length=10)
    complain_against = models.ForeignKey(User, on_delete=models.CASCADE)
