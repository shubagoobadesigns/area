from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class QuestionModel(models.Model):
    question = models.CharField(max_length=256)
    answer_yes = models.CharField(max_length=256)
    answer_no = models.CharField(max_length=256)
    weight_yes = models.FloatField(default=1.0)
    weight_no = models.FloatField(default=1.0)


class ArchetypesModel(models.Model):
    name = models.CharField(max_length=256)


class CheetahSheets(models.Model):
    archetype = models.ForeignKey(ArchetypesModel)
    sheet = models.CharField(max_length=128)


class Problem(models.Model):
    user = models.ForeignKey(User)
    decision_type = models.CharField(max_length=255)
    decision = models.CharField(max_length=255)
    options = models.CharField(max_length=255)
    time_frame = models.CharField(max_length=255)
    decision_type_other = models.CharField(max_length=255)
    success = models.CharField(max_length=255)
    commitment_days = models.IntegerField(default=7)
    commitment = models.TextField()


class ArchType(models.Model):
    problem = models.ForeignKey(Problem)
    arch = models.ForeignKey(ArchetypesModel)
    weight = models.FloatField(default=0)


class Question(models.Model):
    problem = models.ForeignKey(Problem)
    question = models.ForeignKey(QuestionModel, related_name='user_question')
    answer = models.BooleanField(default=False)


class DecisionTypes(models.Model):
    problem = models.ForeignKey(Problem)
    name = models.CharField(max_length=256)

