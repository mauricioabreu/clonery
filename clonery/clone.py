def clone(instance):
    instance.pk = None
    instance.id = None
    instance.save()