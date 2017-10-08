from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=32, null=True, blank=True)
    school = models.CharField(max_length=256)
    grade = models.CharField(max_length=8)
    dream_director = models.CharField(max_length=256, null=True, blank=True)


class QuestionModel(models.Model):
    question = models.CharField(max_length=256, default='')
    answer_yes = models.CharField(max_length=256, null=True)
    answer_no = models.CharField(max_length=256, null=True)
    why = models.CharField(max_length=256, default='')

    @staticmethod
    def get_by_question(question):
        question_models = QuestionModel.objects.filter(question=question).all()
        if len(question_models) > 0:
            return question_models[0]
        else:
            return None

    def text(self):
        return self.question


class ArchetypesModel(models.Model):
    name = models.CharField(max_length=256)


class CheetahSheets(models.Model):
    archetype = models.ForeignKey(ArchetypesModel)
    sheet = models.CharField(max_length=128)


class Problem(models.Model):
    user = models.ForeignKey(User, null=True)
    decision_type = models.CharField(max_length=255)
    decision = models.CharField(max_length=255)
    options = models.CharField(max_length=255)
    time_frame = models.CharField(max_length=255)
    decision_type_other = models.CharField(max_length=255)
    success = models.CharField(max_length=255)
    commitment_days = models.IntegerField(default=7)
    commitment = models.TextField(default='')


class ArchType(models.Model):
    problem = models.ForeignKey(Problem)
    arch = models.ForeignKey(ArchetypesModel)
    weight = models.FloatField(default=0)


class Question(models.Model):
    user = models.ForeignKey(User, null=True)
    session_key = models.CharField(max_length=40, null=True)
    question = models.ForeignKey(QuestionModel, related_name='user_question', null=True)
    answer = models.BooleanField(default=False)

    @staticmethod
    def get_yes_questions(user):
        yes_questions_query = Question.objects.filter(user=user, answer=True)
        return yes_questions_query.all()

    @staticmethod
    def fill_in_user(user, session_key):
        Question.objects.filter(session_key__exact=session_key, user__isnull=True).update(user=user)

    def text(self):
        return self.question.text()


class DecisionTypes(models.Model):
    problem = models.ForeignKey(Problem)
    name = models.CharField(max_length=256)


class CriticalConcepts(models.Model):
    problem = models.OneToOneField(Problem)
    concept1 = models.CharField(max_length=256, default='')
    concept2 = models.CharField(max_length=256, default='')
    concept3 = models.CharField(max_length=256, default='')
