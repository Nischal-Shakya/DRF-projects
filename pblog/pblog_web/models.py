from django.db import models

# Create your models here.


class Id(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    lookingForJob = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
