
from django.db import models
from apps.core.base_model import BaseModel

class SystemSetting(BaseModel):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    description = models.CharField(max_length=255, blank=True)
