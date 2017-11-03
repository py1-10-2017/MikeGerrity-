# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['name']) < 5:
            errors.append("Name field must be > 5 characters")
        if len(post_data['description']) < 15:
            errors.append("Description field must be > 15 characters")
        return errors
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()