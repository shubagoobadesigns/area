from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

from decisions.models import Course, BaseModule
from simple_history.models import HistoricalRecords

class Module3(BaseModule):
    answers = models.TextField(default='')

    @staticmethod
    def num():
        return 3

    # Used to display the number to the user
    # internally it's still module 0
    @staticmethod
    def display_num():
        return 4

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

    @staticmethod
    def get_game_questions():
        game_questions = {
            'behavioral1': {
                'question': 'You failed the test you studied for. You ...',
                'answer0': 'Get upset and rip it up',
                'answer1': 'Schedule a meeting with your teacher',
                'bias': 'behavioral',
                'bias_answer': 0,
                'type0': 'pitfall',
                'type1': 'edge',
            },
            'structural1': {
                'question': "Your sister's favorite store is running a holiday discount but her birthday is not for months. You ...",
                'answer0': 'Buy the gift close to her birthday',
                'answer1': 'Buy the gift at the sale price even though its not near her birthday',
                'bias': 'structural',
                'bias_answer': 0,
                'type0': 'pitfall',
                'type1': 'edge',
            },
            'informational1': {
                'question': 'You are applying to colleges. You ...',
                'answer0': 'Search the school websites and look up costs and class offerings',
                'answer1': 'Look through the school websites but have no real plan and feel overwhelmed',
                'bias': 'informational',
                'bias_answer': 0,
                'type0': 'pitfall',
                'type1': 'edge',
            },
            'analytical1': {
                'question': 'Your history teacher gives you a study sheet for the upcoming test. You ...',
                'answer0': 'Read your notes to help draw conclusions about how to outline answers for each study sheet question',
                'answer1': 'Answer the study sheet questions without using your notes to draw conclusions from them',
                'bias': 'analytical',
                'bias_answer': 0,
                'type0': 'pitfall',
                'type1': 'edge',
            },
        }

        return game_questions

    @staticmethod
    def name():
        return 'Assumptions & Judgements'

    @staticmethod
    def pins():
        pins = [
            'Pin 1',
            'Pin 2',
            'Pin 3',
        ]

        return pins

    def __str__(self):
        to_return = "Module 3 step " + self.step
        if self.completed_on:
            to_return = to_return + " completed on " + str(self.completed_on)
        return to_return

    class Meta:
        verbose_name = 'Module 3 Data'
        verbose_name_plural = 'Module 3 Data'

class Module3Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Module3Form, self).__init__(*args, **kwargs)
        # Not all fields are available all at once so set these to false for now
        self.fields['answers'].required = False

    class Meta:
        model = Module3
        fields = [
            'answers',
                  ]