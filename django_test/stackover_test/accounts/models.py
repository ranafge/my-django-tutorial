from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    bio = models.CharField(default='no bio', max_length=350)

    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users', blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'