# clonery

Django library to clone objects and their relationships

## Features

Here is a list of available features. Unchecked ones are in the roadmap:

- [x] Clone `foreign` relationships
- [x] Clone `many to many` relationships
- [x] Ignore fields from being cloned

## How to use

```python
import clonery

from models import Person

person = Person.objects.get(id=1)

clonery.clone(person)
```
