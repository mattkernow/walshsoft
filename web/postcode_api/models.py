from django.contrib.gis.db import models


class Postcode(models.Model):
    """Postcode model."""
    postcode = models.CharField(max_length=8)
    geom = models.PointField(srid=27700)
