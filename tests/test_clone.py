import pytest

import clonery
from .models import (
    Album, Track, Discography)


def test_clone():
    album = Album.objects.create(name="Fear of the dark")
    clonery.clone(album)
    assert Album.objects.count() == 2

    cloned = Album.objects.get(id=2)
    assert cloned.name == "Fear of the dark"


def test_clone_relationship():
    album = Album.objects.create(name="Fear of the dark")
    track = Track.objects.create(album=album, title="Wasting love", number=9)
    clonery.clone(track)

    assert Track.objects.count() == 2
    assert Album.objects.count() == 2


def test_clone_many_to_many():
    worst_album = Album.objects.create(name="Virtual XI")
    best_album = Album.objects.create(name="The number of the beast")
    discography = Discography.objects.create(title="The best and the worst of Iron Maiden")
    discography.related.add(worst_album)
    discography.related.add(best_album)

    clonery.clone(discography)
    assert Discography.objects.count() == 2
    assert Album.objects.count() == 4


def test_clone_unsaved_instance():
    album = Album(name="Powerslave")
    with pytest.raises(clonery.UnsavedObject):
        clonery.clone(album)
