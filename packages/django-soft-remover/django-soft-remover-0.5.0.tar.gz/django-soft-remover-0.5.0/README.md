# django-soft-remover

[![GitHub Actions](https://github.com/pikhovkin/django-soft-remover/workflows/build/badge.svg)](https://github.com/pikhovkin/django-soft-remover/actions)
[![PyPI](https://img.shields.io/pypi/v/django-soft-remover.svg)](https://pypi.org/project/django-soft-remover/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-soft-remover.svg)
[![framework - Django](https://img.shields.io/badge/framework-Django-0C3C26.svg)](https://www.djangoproject.com/)
![PyPI - Django Version](https://img.shields.io/pypi/djversions/django-soft-remover.svg)
[![PyPI - License](https://img.shields.io/pypi/l/django-soft-remover)](./LICENSE)

Abstract Django models for soft removal.

It supports unique field indices specified with
- `unique`
- `unique_together`
- `UniqueConstraint` (without expressions or conditions)

Just add the `remver` field to the composite unique index if you need to maintain uniqueness between removed versions.

### Installation

```bash
$ pip install django-soft-remover
```

### Example of use

```python
from django.db import models

from soft_remover.models import SoftRemovableModel, SoftRestorableModel


class ManyUniqueTogetherRem(SoftRemovableModel):
    category = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    tag = models.CharField(max_length=32)
    value = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (('category', 'name', 'remver'), ('category', 'tag', 'remver'))

        
class UniqueWithConstraint(SoftRemovableModel):
    name = models.CharField(max_length=32)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'remver'], name='uwc_name_remver'),
        ]

        
class ManyUniqueTogetherRes(SoftRestorableModel):
    category = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    tag = models.CharField(max_length=32)
    value = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (('category', 'name'), ('category', 'tag'))
```

See more examples in [test models](https://github.com/pikhovkin/django-soft-remover/blob/master/soft_remover/tests/models.py).

### License

MIT
