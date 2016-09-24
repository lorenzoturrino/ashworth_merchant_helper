from __future__ import unicode_literals

from django.db import models


class Processor(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ApiKey(models.Model):
    key = models.CharField(max_length=255)
    processor = models.ForeignKey(Processor, related_name='api_keys')

    def __str__(self):
        return self.processor.name + ' payment API'