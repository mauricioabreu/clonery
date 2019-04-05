from django.db import models


class DummyModel(models.Model):
    """Base model for testing."""
    
    text = models.CharField(
        max_length=100,
        verbose_name="char field"
    )


class DummyModelWithForeignKey(models.Model):
    """Model to test foreign key relantionships."""

    number = models.IntegerField()
    related = models.ForeignKey(DummyModel, on_delete=models.CASCADE)