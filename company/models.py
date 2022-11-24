from django.db import models
import uuid

# Create your models here.
class Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.IntegerField()
    date = models.DateField()
    value = models.FloatField()
    cpf = models.CharField(max_length=11)
    credit_card = models.CharField(max_length=12)
    hour = models.TimeField()
    owner_company = models.CharField(max_length=50)
    name_company = models.CharField(max_length=50)
