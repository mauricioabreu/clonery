# clonery

Django library to clone objects and their relationships

## How to use

```python
import clonery

from models import Person

person = Person.objects.get(id=1)

clonery.clone(person)
```