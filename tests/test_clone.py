import clonery
from .models import DummyModel


def test_clone():
    original = DummyModel.objects.create(text="it must be cloned")
    clonery.clone(original)
    assert DummyModel.objects.count() == 2

    cloned = DummyModel.objects.get(id=2)
    assert cloned.text == "it must be cloned"