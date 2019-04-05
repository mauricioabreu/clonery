def clone(instance):
    if not instance.pk:
        raise UnsavedObject

    for field in instance._meta.get_fields():
        if field.many_to_one:
            related_instance = getattr(instance, field.name)
            related_instance.pk = None
            related_instance.id = None
            related_instance.save()
    instance.pk = None
    instance.id = None
    instance.save()


class UnsavedObject(Exception):
    """Raise when trying to clone an unsaved object."""
    pass
