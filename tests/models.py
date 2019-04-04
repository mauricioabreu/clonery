from django.db import models


class DummyModel(models.Model):
    """Base model for testing."""
    
    text = models.CharField(
        max_length=100,
        verbose_name="char field"
    )