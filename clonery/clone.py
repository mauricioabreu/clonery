def clone(instance, **options):
    ignored = options.get('ignored', [])

    if not instance.pk:
        raise UnsavedObject

    for field in instance._meta.get_fields():
        if field.name in ignored:
            # TODO(mauricioabreu): what happens if there is no default?
            setattr(instance, field.attname, field.get_default())

        if field.many_to_one:
            related_instance = getattr(instance, field.name)
            related_instance.pk = None
            related_instance.id = None
            related_instance.save()
        if field.many_to_many and not field.auto_created:
            related_manager = getattr(instance, field.name)
            related_instances = related_manager.all()
            for related_instance in related_instances:
                related_instance.pk = None
                related_instance.id = None
                related_instance.save()

    instance.pk = None
    instance.id = None
    instance.save()


class UnsavedObject(Exception):
    """Raise when trying to clone an unsaved object."""
    pass
