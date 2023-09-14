from django.db import models
from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel
from utils.model import Model
from ckeditor.fields import RichTextField

# Create your models here.
class Post(Model, ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel):
    class Meta:
        verbose_name_plural = "Blogs"

    body = RichTextField()