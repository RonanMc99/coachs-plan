from django.db import models

class Coach(models.Model):
    ''' Coachs create the Plans '''
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Plan(models.Model):
    ''' Plans are available for purchase '''
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    slug = models.SlugField()
    image = models.ImageField()
    price = models.FloatField()
    plan_id = models.CharField(max_length=10)
    created_by = models.ManyToManyField(Coach)

    def __str__(self):
        return self.title
