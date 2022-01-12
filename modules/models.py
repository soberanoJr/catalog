from django.db import models

# Create your models here.
class Module(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"Module #{self.id}: {self.name}"


class Lesson(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateField()
    module = models.ManyToManyField(Module, blank=True, related_name="lessons")
    link = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name} | {self.date}"