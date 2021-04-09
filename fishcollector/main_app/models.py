from django.db import models

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

class Fish (models.Model):
    name = models.CharField(max_length = 100)
    specie = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)



class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField('meals', max_length=1, choices=MEALS, default=MEALS[0][0])
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)