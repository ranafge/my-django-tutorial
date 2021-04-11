from django.db import models


# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=200, verbose_name='verbose name')

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(verbose_name='verbose name Title', max_length=120 )
    details = models.TextField(verbose_name='verbose name Details/Description', blank=False)
    people = models.ManyToManyField(
        People,
        through='PeopleGame',
        related_name='games'
    )


class PeopleGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    scroe = models.CharField(max_length=5)

    def __str__(self):
        return f'Game : {self.game.title}, Person: {self.person} score: {self.scroe}'