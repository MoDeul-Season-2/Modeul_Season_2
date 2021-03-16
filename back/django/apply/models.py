from django.db import models
from core import models as core_models


class Apply(core_models.TimeStampedModel):
    applyName = models.CharField(max_length=50)
    house = models.CharField(max_length=100)
    host = models.CharField(max_length=50)
    guest = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.house

    class Meta:
        verbose_name_plural = "Applies"