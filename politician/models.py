# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class PoliticalParty(models.Model):
    number = models.IntegerField(null=False, primary_key=True, auto_created=False)
    name = models.CharField(max_length=255, null=False)
    initials = models.CharField(max_length=10, null=False)
    vision = models.TextField(max_length=1000, null=False)
    picture = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return u"%d - %s" % (self.number, self.initials)


class Politician(models.Model):
    name = models.CharField(max_length=255, null=False)
    gender = models.CharField(max_length=45, null=False)
    political_party = models.ForeignKey(PoliticalParty, on_delete=models.SET_NULL, null=True)
    about = models.TextField(max_length=1000, null=False)
    picture = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return u"%s (%s)" % (self.name, self.political_party.initials)
