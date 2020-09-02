from django.db import models

class Coach(models.Model):
    ''' Coachs create the Plans '''
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = 'Coaches'


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


class Section(models.Model):
    ''' Plans are divided into sections '''
    title = models.CharField(max_length=150)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    section_number = models.IntegerField()

    def __str__(self):
        return self.title


class Activity(models.Model):
    ''' Sections contain user activities / todos '''
    title = models.CharField(max_length=150)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    activity_number = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Activities'


class Example(models.Model):
    ''' Examples of completed activities '''
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    solution_number = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return f"{self.activity}-{self.pk}"