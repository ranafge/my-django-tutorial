from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.conf import settings
from  django.db import models

from taggit.managers import TaggableManager

class Food(models.Model):
    food_name = models.CharField(max_length=120)
    tags = TaggableManager()

class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='up/', blank=True, null=True)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class WorkTime(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="work_times")
    work_start = models.DateTimeField()
    work_end = models.DateTimeField()
    work_delta = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.work_delta = (self.work_end - self.work_start).seconds
        super().save(*args, **kwargs)




