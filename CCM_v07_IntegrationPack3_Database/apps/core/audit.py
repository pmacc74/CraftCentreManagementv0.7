
from django.db import models
from .base_model import BaseModel

class AuditEntry(BaseModel):
    module = models.CharField(max_length=50)
    action = models.CharField(max_length=100)
    username = models.CharField(max_length=150)
    details = models.TextField(blank=True)
