from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False)
    image = models.ImageField(upload_to='')
    release_date = models.DateField(null=False)
    lte_exists = models.BooleanField(null=False)
    slug = models.SlugField(null=False, unique=True)

