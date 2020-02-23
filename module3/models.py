# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

from decisions.models import Course, BaseModule
from simple_history.models import HistoricalRecords

# Create your models here.
class Module3(BaseModule):
    answers = models.TextField(default='')
    # at = absolute targets
    at = models.TextField(default='')
    # absolute targets checklist
    at2 = models.TextField(default='')
    # absolute target most useful
    at2_most = models.TextField(default='')
    at3 = models.TextField(default='')
    at3_most = models.TextField(default='')
    # cc = critical concepts
    cc = models.TextField(default='')
    dd_as_question = models.TextField(default='')
    feeling_end = models.TextField(default='')
    feeling_start = models.TextField(default='')
    pro_con_least = models.TextField(default='')
    pro_con_most = models.TextField(default='')
    problem_to_solve = models.TextField(default='')
    # vs = vision of success
    vs = models.TextField(default='')

    @staticmethod
    def num():
        return 3

    # For the time being only save the cheetah sheet answers
    # If you have to add/remove fields from this list, make sure to re-run
    # ./manage.py makemigrations && ./manage.py migrate to update the history model
    excluded_fields = [
        'step',
        'completed_on',
    ]
    history = HistoricalRecords(excluded_fields=excluded_fields)

    def save_without_historical_record(self, *args, **kwargs):
        self.skip_history_when_saving = True
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret

    # Used to display the number to the user
    # internally it's still module 0
    @staticmethod
    def display_num():
        return 4

    @staticmethod
    def name():
        return 'Backpocket AREA'

    def __str__(self):
        to_return = "Module 3 step " + self.step
        if self.completed_on:
            to_return = to_return + " completed on " + str(self.completed_on)
        return to_return

    @staticmethod
    def get_at2_numbers():
        at_numbers = [
            {
                'key': "1",
                'label': "I located numerical data that is useful to better understanding my Target(s)",
                'answer': "Good! Numbers allow you to see the Target as objectively and uninfluenced as possible.",
            },
            {
                'key': "2",
                'label': "The numerical data I found was not relevant to the problem I am solving.",
                'answer': "Might your Target not provide relevant data for a reason? Or, might it lack transparency?",
            },
            {
                'key': "3",
                'label': "The numerical data I found did not make sense.",
                'answer': "Why might the numbers not make sense? Could this mean the Target is trying to hide something or is going through some kind of transition?",
            },
            {
                'key': "4",
                'label': "The numerical data tells a story about my Target(s).",
                'answer': "Good! That means you may consider if the story that you understand about the Target is consistent with its numerical story.",
            },
        ]

        return at_numbers

    @staticmethod
    def get_at3_numbers():
        at_numbers = [
            {
                'key': "1",
                'label': "I more clearly understand how the Target perceives its value",
                'answer': "You can consider whether your Target’s perception of value matches what you expected",
            },
            {
                'key': "2",
                'label': "I don't understand how the Target perceives its value",
                'answer': "You have some questions about your Target’s credibility",
            },
            {
                'key': "3",
                'label': "It makes me want to question part of my Target's story",
                'answer': "You need more research to understand your Target",
            },
        ]

        return at_numbers

    @staticmethod
    def get_biases():
        biases = [
            {
                'key': 'harmful',
                'label': 'Harmful',
                'action': 'This bias is less likely but might be at work if an authority figure in your life is favorable towards Ohio State.',
                'definition': 'The tendency to take on the opinion of someone who is seen as an authority figure',
                'cheetah4': 'Might you be impacted by an authority figure?',
            },
            {
                'key': 'long_term',
                'label': 'Long Term Impact',
                'action': 'This bias might be at work if you know someone who also likes it.',
                'definition': 'Gravitating toward things and people we like',
                'cheetah4': 'Are you gravitating toward things and people you like?',
            },
            {
                'key': 'outcome',
                'label': 'Outcome',
                'action': 'This bias is not relevant because it is about underestimating how long a task will take even if we have done it before.',
                'definition': "Underestimating how long a task will take, even if you've done it before",
                'cheetah4': 'Might you be making an assumption about the time to complete a task?',
            },
        ]

        return biases

    @staticmethod
    def get_ddd_parameters():
        ddd_parameters = [
            {
                'key': 'outcome',
                'question': "do you have a sense of how this decision will play out",
                'labels': [ 'Unlikely', 'Somewhat Unlikely', 'Very Likely' ],
            },
            {
                'key': 'outcome',
                'question': "are you stumped",
                'labels': ['Unlikely', 'Somewhat Unlikely', 'Very Likely'],
            },
            {
                'key': 'long_term',
                'question': "does the problem weigh on you",
                'labels': ['No impact', 'Some impact', 'Long term impact'],
            },
        ]

        return ddd_parameters


    @staticmethod
    def get_game_questions():
        game_questions = {
            'outcome1': {
                'question': 'Do you have a sense of how this decision will play out?',
                'answer0': 'Yes',
                'answer1': 'No',
                'bias': 'outcome',
                'bias_answer': 0,
                'yes': "Let's check your gut assumptions with evidence. Just be careful of your own biases; it may make you less open-minded to disconfirming evidence.",
                'no': "Let's find some information to help you better understand the implications of your outcome options",
            },
            'outcome2': {
                'question': 'Are you stumped?',
                'answer0': 'Yes',
                'answer1': 'No',
                'bias': 'outcome',
                'bias_answer': 0,
                'yes': "Let's find some information to help you better understand the implications of your outcome options",
                'no': "Let's check your gut assumptions with evidence",
            },
            'long_term1': {
                'question': 'Does the problem weigh on you?',
                'answer0': 'Yes',
                'answer1': 'No',
                'bias': 'long_term',
                'bias_answer': 0,
                'yes': "Let's check your gut’s feelings with evidence",
                'no': "How important a decision is it for you?",
            },
            'long_term2': {
                'question': 'Do you have a deadline in which to make this decision?',
                'answer0': 'Yes',
                'answer1': 'No',
                'bias': 'long_term',
                'bias_answer': 0,
                'yes': "Let's find some information to help you better understand the implications of your outcome options",
                'no': "Let's take the time to gather some information to help you better understand the implications of your outcome options",
            },
            'harmful1': {
                'question': 'Will this decision set you on a specific path that will crowd out other options?',
                'answer0': 'Yes',
                'answer1': 'No',
                'bias': 'harmful',
                'bias_answer': 0,
                'yes': "Let's check your gut assumption with evidence.",
                'no': "Let's take the time to gather some information to help you better understand the implications of your outcome options",
            },
            'harmful2': {
                'question': 'If you make the wrong decision, do you worry you’ll have regrets?',
                'answer0': 'Yes',
                'answer1': 'No',
                'bias': 'harmful',
                'bias_answer': 0,
                'yes': "Let's check your gut assumption with evidence.",
                'no': "Let's take the time to gather some information to help you better understand the implications of your outcome options",
            },
            'outcome3': {
                'question': 'Are you being heavily influenced by others to choose one outcome?',
                'answer0': 'Yes',
                'answer1': 'No',
                'bias': 'outcome',
                'bias_answer': 0,
                'yes': "What are the incentives of the people trying to influence your outcome?",
                'no': "Let's find some information to help you better understand the implications of your outcome options",
            },
            'harmful3': {
                'question': 'Would a poor decision be costly to you?',
                'answer0': 'Yes',
                'answer1': 'No',
                'bias': 'harmful',
                'bias_answer': 0,
                'yes': "Let's check your assumption with evidence.",
                'no': "Let's take the time to gather some information to help you better understand the implications of your outcome options",
            },
        }

        return game_questions

    @staticmethod
    def get_relative_map():
        relative_map = [
            {
                'label': "I understand my Target's point of differentiation from competitors",
            },
            {
                'label': "I understand my Target's strengths versus its competitors",
            },
            {
                'label': "I understand my Target's weaknesses versus its competitors",
            },
            {
                'label': "The public image of my Target is consistent with the way the Target described itself in Absolute",
            },
        ]

        return relative_map

    class Meta:
        verbose_name = "Module 4 Data - Backpocket AREA"
        verbose_name_plural = "Module 4 Data - Backpocket AREA"

class Module3Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Module3Form, self).__init__(*args, **kwargs)
        # Not all fields are available all at once so set these to false for now
        # If you forget to set the .required to false, you'll get a
        # django 'bool' object has no attribute 'disabled' error
        self.fields['answers'].required = False
        self.fields['at'].required = False
        self.fields['at2'].required = False
        self.fields['at2_most'].required = False
        self.fields['at3'].required = False
        self.fields['at3_most'].required = False
        self.fields['cc'].required = False
        self.fields['dd_as_question'].required = False
        self.fields['feeling_start'].required = False
        self.fields['feeling_end'].required = False
        self.fields['pro_con_least'].required = False
        self.fields['pro_con_most'].required = False
        self.fields['problem_to_solve'].required = False
        self.fields['vs'].required = False


    class Meta:
        model = Module3
        fields = ['answers',
                  'at',
                  'at2',
                  'at2_most',
                  'at3',
                  'at3_most',
                  'cc',
                  'dd_as_question',
                  'feeling_end',
                  'feeling_start',
                  'pro_con_least',
                  'pro_con_most',
                  'problem_to_solve',
                  'vs',
                  ]