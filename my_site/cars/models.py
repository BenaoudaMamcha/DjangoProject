from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Cars(models.Model):
    name=models.CharField(_("matricule"), max_length=50)
    brand = models.CharField(_("marque"), max_length=50, null=True)