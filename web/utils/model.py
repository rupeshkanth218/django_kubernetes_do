from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

class Model(models.Model):
    id = models.UUIDField(
        _('id'),
        primary_key=True,
        default=uuid.uuid4
    )

    class Meta:
        abstract = True