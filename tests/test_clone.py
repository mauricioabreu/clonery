import pytest

import clonery
from .models import DummyModel, DummyModelWithForeignKey


def test_clone():
    original = DummyModel.objects.create(text="it must be cloned")
    clonery.clone(original)
    assert DummyModel.objects.count() == 2

    cloned = DummyModel.objects.get(id=2)
    assert cloned.text == "it must be cloned"


def test_clone_relationship():
    model_to_relate = DummyModel.objects.create(text="it must be cloned")
    related_instance = DummyModelWithForeignKey.objects.create(related=model_to_relate, number=42)
    clonery.clone(related_instance)

    assert DummyModelWithForeignKey.objects.count() == 2
    assert DummyModel.objects.count() == 2


def test_clone_unsaved_instance():
    original = DummyModel(text="it must be cloned")
    with pytest.raises(clonery.UnsavedObject):
        clonery.clone(original)
