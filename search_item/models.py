from django.db import models

# Create your models here.


class Information(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "informations"

    def __str__(self):
        return self.name
