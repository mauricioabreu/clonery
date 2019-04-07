import pytest

import clonery
from .models import (
    DummyModel, DummyModelWithForeignKey, DummyModelManyToMany)


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


def test_clone_many_to_many():
    one_thing = DummyModel.objects.create(text="one relation")
    another_thing = DummyModel.objects.create(text="another relation")
    many_to_many = DummyModelManyToMany.objects.create(text="i have a lot of related objects")
    many_to_many.related.add(one_thing)
    many_to_many.related.add(another_thing)

    clonery.clone(many_to_many)
    assert DummyModelManyToMany.objects.count() == 2
    assert DummyModel.objects.count() == 4


def test_clone_unsaved_instance():
    original = DummyModel(text="it must be cloned")
    with pytest.raises(clonery.UnsavedObject):
        clonery.clone(original)
