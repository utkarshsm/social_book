from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    public_visibility = models.BooleanField(default=False)
    age = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=50,null=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='cover/')
    pdf = models.FileField(upload_to='pdf/')

    def delete(self, *args, **kwargs):
        self.cover.delete()
        self.pdf.delete()
        super(Book, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title