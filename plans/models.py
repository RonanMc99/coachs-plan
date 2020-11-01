from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.shortcuts import reverse, redirect


class UsersPlans(models.Model):
    """ A list of plans that the user has access to """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plans = models.ManyToManyField('Plan', blank=True)

    def __str__(self):
        return self.user.username

    def plans_list(self):
        return self.plans.all()

    class Meta:
        verbose_name = "User's Plans"
        verbose_name_plural = "User's Plans"


# Use a signal to create an instance on signup
def post_user_signup_receiver(sender, instance, created, *args, **kwargs):
    if created:
        UsersPlans.objects.get_or_create(user=instance)

post_save.connect(post_user_signup_receiver, sender=settings.AUTH_USER_MODEL)

class Coach(models.Model):
    """ Represents a 'coach' user.
        Coaches are users who create and administer the plans. 
    """

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    blurb = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("blog:coach-view", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = "Coaches"


class Plan(models.Model):
    """ Plans are available for purchase
        A plan is created by a coach, and represents a collection of end-user activities.
        Examples may include 7 days of exercise routines or a set of meal plans. 
    """

    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateTimeField()
    slug = models.SlugField()
    image = models.ImageField()
    price = models.FloatField()
    plan_id = models.CharField(max_length=10)
    created_by = models.ManyToManyField(Coach)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("plans:plan-details", kwargs={"slug": self.slug})


class Section(models.Model):
    """ Sections group together activites within a plan.
        Sections may represent one day at the gym or one 24 hour period for nutrition planning. 
        Breadcrumb trails use sections within the navigation.
    """

    title = models.CharField(max_length=150)
    description = description = models.TextField(blank=True, default="Section Description")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    section_number = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "plans:section-details",
            kwargs={"plan_slug": self.plan.slug, "section_number": self.section_number},
        )


class Activity(models.Model):
    """ An activity represents the specific actions assigned to a user within a plan.
        Examples may include a set of workout instructions or a nutritional protocol
    """

    activity_title = models.CharField(max_length=150)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    activity_number = models.IntegerField()
    activity_description = models.TextField()
    activity_image = models.ImageField(null=True, blank=True)
    activity_video = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.activity_title

    def get_absolute_url(self):
        return reverse(
            "plans:activity-details",
            kwargs={
                "plan_slug": self.section.plan.slug,
                "section_number": self.section.section_number,
                "activity_number": self.activity_number,
            },
        )

    class Meta:
        verbose_name_plural = "Activities"


class Example(models.Model):
    """ Example documents related to the activity
    Such as: workout instructions, charts, downloadable menus, meal plans
    Any collateral linked to the activity can be linked as img or pdf
    """

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    example_title = models.CharField(max_length=150)
    example_description = models.TextField(blank=True)
    example_number = models.IntegerField()
    example_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.activity.activity_title}-{self.pk}"
