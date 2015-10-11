from django.db import models
from django.db.models import Model

class Item(Model):
    text = models.TextField(default='')