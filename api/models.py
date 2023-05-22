from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postalcode = models.CharField(max_length=100)

    def __str__(self):
        return self.street

class Distance(models.Model):
    distance = models.CharField(max_length=100)
    destination = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        primary_key=False,
        null=True,
        related_name='destination'
    )
    source = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        primary_key=False,
        null=True,
        related_name='source'
    )

    def __str__(self):
        return self.source.street