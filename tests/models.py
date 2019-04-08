from django.db import models


class Album(models.Model):
    """Base model for testing."""

    name = models.CharField(
        max_length=100,
        verbose_name="Album name"
    )


class Track(models.Model):
    """Model to test foreign key relationships."""

    title = models.CharField(
        max_length=100,
        verbose_name="Track title"
    )
    number = models.IntegerField(default=0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


class Discography(models.Model):
    """Model to test many to many relationships."""

    title = models.CharField(
        max_length=100,
        verbose_name="Discography title"
    )
    related = models.ManyToManyField(Album)
