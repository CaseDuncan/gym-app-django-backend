from django.db import models

# Create your models here.
class Service(models.Model):
    SERVICES_CHOICES = (
        ("Zomba","Zomba"),
        ("Yoga", "Yoga"),
    )
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Plan(models.Model):
    PLANS_CHOICES=(
        ("Monthly","Monthly"),
        ("Weekly","Weekly"),
        ("Daily","Daily")
    )
    plan_type = models.CharField(max_length=100, choices=PLANS_CHOICES,null=False, blank=False)
    description = models.TextField()

    def __str_(self):
        return self.plan_type

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"