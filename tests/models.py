from django.db import models


class DummyModel(models.Model):
    """Base model for testing."""

    text = models.CharField(
        max_length=100,
        verbose_name="char field"
    )


class DummyModelWithForeignKey(models.Model):
    """Model to test foreign key relationships."""

    number = models.IntegerField()
    related = models.ForeignKey(DummyModel, on_delete=models.CASCADE)


class DummyModelManyToMany(models.Model):
    """Model to test many to many relationships."""

    text = models.CharField(
        max_length=100,
        verbose_name="char field"
    )
    related = models.ManyToManyField(DummyModel)
