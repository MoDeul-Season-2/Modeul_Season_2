from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    name = models.CharField(max_length=80)
    subtitle = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Amenity(AbstractItem):

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    class Meta:
        verbose_name_plural = "Facilities"


class Photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=80)

    file = models.ImageField(upload_to="house_photos")
    house = models.CharField(max_length=80)

    def __str__(self):
        return self.caption


class House(core_models.TimeStampedModel):
    name = models.CharField(max_length=130)
    description = models.TextField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=120)
    amenities = models. ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    host = models.CharField(max_length=80)
    photo = models.ForeignKey("Photo", related_name="photo", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)
