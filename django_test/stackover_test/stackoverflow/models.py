from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published = models.BooleanField(False)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_number_of_work_items(self):
        return self.applicant_set.count()

class Applicant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    country = CountryField(blank_label='(select country)', blank=True, null=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='up/', blank=True, null=True)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url



    def __str__(self):
        return self.name




class Pattern(models.Model):
    patternName = models.CharField(max_length=64)

    def __str__(self):
        return self.patternName


class Part(models.Model):
    unitsList = (
        ('szt', "szt"),
        ('m', "m"),
        ('komp', "komp")
    )
    partName = models.CharField(unique=False, max_length=128)
    code = models.CharField(unique=True, max_length=15)
    units = models.CharField(max_length=10, choices=unitsList, default='szt')
    description = models.TextField()
    pattern = models.ManyToManyField(Pattern, related_name='patterns')


class Post(models.Model):
    text = models.TextField()
    likes = models.ManyToManyField(User, related_name='realtednamepost')
    status = models.CharField(max_length=1, default=1)
    created_on = models.DateTimeField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField(max_length=250)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.name = self.name.capitalize()
        super().save(**kwargs)




class A(models.Model):
    x = models.CharField(blank=True, null=True, max_length=256)
    y = models.CharField(blank=True, null=True, max_length=256)

    def __str__(self):
        return f'{self.x} - {self.y}'


class B(models.Model):
    m = models.ManyToManyField(to=A, blank=True)
    #other fields

class C(models.Model):
    p = models.ManyToManyField(to=A, blank=True)


class PersonScore(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    person = models.ForeignKey("Person", on_delete=models.CASCADE)

    def __str__(self):
        return self.person.name


class Person(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PersonType(models.Model):
    person = models.ForeignKey("Person",on_delete=models.CASCADE)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type
    
 # Person.objects.prefetch_related('persontype_set').all()
# PersonScore.objects.select_related('person')
# instance = Person.objects.first()
# instance.persontype_set.all()
# <QuerySet [<PersonType: type male big>]>


class  Room(models.Model):
	ROOM_TYPES = (
		(1, 'Single'),
		(2, 'Double'),
		(3, 'Triple'),
	)
	
	name = models.CharField(max_length=50)
	status = models.CharField(max_length=30, blank=True)
	room_number = models.IntegerField(blank=True, null=True)
	nobeds = models.IntegerField(blank=True, null=True)
	room_type = models.PositiveSmallIntegerField(choices=ROOM_TYPES)


# Readonly filed or disable so that it can't be editable.

class Item(models.Model):
    sku = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    default = models.CharField(max_length=150, default='this is my default', null=True, blank=True)

    @property
    def table_name(self):
        return self._meta.db_table


    def __str__(self):
        return f'sku is the {self.sku}'


