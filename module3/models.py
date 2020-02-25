# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

from decisions.models import Course, BaseModule
from simple_history.models import HistoricalRecords

# List of all of the DB fields for this module
db_fields = [
    'answers',
    'at',
    'at2',
    'at2_most',
    'at3',
    'at3_most',
    'br',
    'cc',
    'dd_as_question',
    'dd_params',
    'feeling_end',
    'feeling_start',
    'pro_con_least',
    'pro_con_most',
    'problem_to_solve',
    'success_terms',
    'vs',
]

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
    # br = bias remedies
    br = models.TextField(default='')
    # cc = critical concepts
    cc = models.TextField(default='')
    dd_as_question = models.TextField(default='')
    # decision dilemma parameters
    dd_params = models.TextField(default='')
    feeling_end = models.TextField(default='')
    feeling_start = models.TextField(default='')
    pro_con_least = models.TextField(default='')
    pro_con_most = models.TextField(default='')
    problem_to_solve = models.TextField(default='')
    success_terms = models.TextField(default='')
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
                'labels': [ 'No', 'Somewhat', 'Yes' ],
                'values': [1, 2, 3],
            },
            {
                'key': 'outcome',
                'question': "are you stumped",
                'labels': ['No', 'Somewhat', 'Yes'],
                'values': [1, 2, 3],
            },
            {
                'key': 'long_term',
                'question': "does the problem weigh on you",
                'labels': ['No', 'Somewhat', 'Yes'],
                'values': [1, 2, 3],
            },
            {
                'key': 'long_term',
                'question': "do you have a deadline in which to make this decision",
                'labels': ['No', 'Somewhat', 'Yes'],
                'values': [1, 2, 3],
            },
            {
                'key': 'harmful',
                'question': "will this decision set you on a specific path that will crowd out other options",
                'labels': ['Harmless', 'Some impact', 'Harmful'],
                'values': [1, 2, 3],
            },
            {
                'key': 'harmful',
                'question': "do you worry you’ll have regrets if you make the wrong decision",
                'labels': ['Harmless', 'Some impact', 'Harmful'],
                'values': [1, 2, 3],
            },
            {
                'key': 'outcome',
                'question': "are you being heavily influenced by others to choose one outcome",
                'labels': ['Not influenced', 'Some influence', 'Heavily influenced'],
                'values': [1, 2, 3],
            },
            {
                'key': 'harmful',
                'question': "would a poor decision be costly to you",
                'labels': ['Not costly', 'Somewhat costly', 'Very costly'],
                'values': [1, 2, 3],
            },
        ]

        return ddd_parameters


    @staticmethod
    def get_game_questions():
        game_questions = {
            'projection1': {
                'question': 'You see tickets for your favorite band playing a show nearby. Do you',
                'answer0': 'Buy two tickets, of course your friend will want to come',
                'answer1': 'Ask your friend before commiting her to buying them',
                'bias': 'projection',
                'bias_answer': 0,
            },
            'authority1': {
                'question': 'A co-worker who has been around much longer than you shows you how to complete a task &quot;the way it has always been done.&quot;',
                'answer0': 'Follow his advice - he has been there a long time',
                'answer1': 'Try out new ways - you never know if you don’t try!',
                'bias': 'authority',
                'bias_answer': 0,
            },
            'authority2': {
                'question': 'Your landlord suggests that you commit to your lease for another year, do you',
                'answer0': 'Automatically resign',
                'answer1': 'Look around before you recommit',
                'bias': 'authority',
                'bias_answer': 0,
            },
            'authority3': {
                'question': 'Recently all your friends joined the same gym, do you',
                'answer0': 'Join right alongside them',
                'answer1': 'Stick with running outside',
                'bias': 'long_term',
                'bias_answer': 0,
            },
            'liking1': {
                'question': 'You get nervous when you have to talk in front of people but your friend asks you to perform in an open mic night with her. Do you',
                'answer0': 'Say yes because they are your friend',
                'answer1': 'Say no because it isn’t your thing',
                'bias': 'liking',
                'bias_answer': 0,
            },
            'optimism1': {
                'question': 'You just applied for a new job, do you',
                'answer0': 'Assume you’re an above average candidate',
                'answer1': 'Assume the pool of candidates is full of competition',
                'bias': 'optimism',
                'bias_answer': 0,
            },
            'liking2': {
                'question': 'Your local grocery store has banned plastic bags. Do you',
                'answer0': 'Assume your friends and neighbors feel the same way you do',
                'answer1': "Ask around to find out other people's opinions",
                'bias': 'liking',
                'bias_answer': 0,
            },
            'planning1': {
                'question': 'You have a big interview in two days. Do you',
                'answer0': 'Review the company and make a list of questions so you can prepare tomorrow',
                'answer1': 'Figure you’re good on your feet and tomorrow night will be enough time',
                'bias': 'planning',
                'bias_answer': 0,
            },
            'optimism2': {
                'question': 'You buy a new car and are considering getting AAA, do you',
                'answer0': 'Absolutely get it - you never know what could happen',
                'answer1': 'Assume you’ll be able to figure it out if anything happens',
                'bias': 'optimism',
                'bias_answer': 0,
            },
            'planning2': {
                'question': 'When you look at your to do list, do you',
                'answer0': 'Start at the top and work your way down until you’re out of time',
                'answer1': 'Go through the list and prioritize items to get done first',
                'bias': 'planning',
                'bias_answer': 0,
            },
            'social1': {
                'question': 'You hear co-workers are going to leave work early on a sunny day, do you',
                'answer0': 'Go along with them, the whole office is',
                'answer1': 'Stick behind, you don’t follow crowds',
                'bias': 'social',
                'bias_answer': 0,
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

    @staticmethod
    def get_success_terms():
        return [
            {
                'question': "A sense of personal agency",
                'explanation': "I want to feel an increase sense of personal agency",
                'phrase': 'empowered',
            },
            {
                'question': "That I didn’t rush to judgment",
                'explanation': "I want to better spot and challenge assumptions and judgments",
                'phrase': "I didn't rush to judgment",
            },
            {
                'question': "That I have a clear direction",
                'explanation': "I want to be able to know how to implement my decision",
                'phrase': 'A clear sense of direction',
            },
            {
                'question': "That I am knowledgeable about next steps",
                'explanation': "I want to learn AREA and build my decision-making skill set",
                'phrase': 'Knowledgeable about the next steps to take',
            },
            {
                'question': "That I looked at the problem from a variety of perspectives",
                'explanation': "I want to know that I checked my ego and examined other voices",
                'phrase': 'That I looked at the problem from a variety of perspectives',
            },
            {
                'question': "That I am enhancing harmony with others",
                'explanation': "I want to strengthen my relationship with others by solving my problem holistically",
                'phrase': 'Harmony with others',
            },
            {
                'question': "A sense of relief that I solved my problem",
                'explanation': "I want a sense of closure",
                'phrase': 'Relief that I solved my problem',
            },
            {
                'question': "Confident that I strengthened my decision-making capabilities",
                'explanation': "I want to be a more confident decision-maker",
                'phrase': 'Confidence that I strengthened my decision-making capabilities',
            },
            {
                'question': "That I chose the right option for me",
                'explanation': "I want to feel an Increase in self-efficacy",
                'phrase': 'Conviction that I chose the right option for me',
            },
            {
                'question': "Stay true to my values",
                'explanation': "I want to identify what matters most to me",
                'phrase': 'True to my values',
            },
        ]

    class Meta:
        verbose_name = "Module 4 Data - Backpocket AREA"
        verbose_name_plural = "Module 4 Data - Backpocket AREA"

class Module3Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Module3Form, self).__init__(*args, **kwargs)
        # Not all fields are available all at once so set these to false for now
        # If you forget to set the .required to false, you'll get a
        # django 'bool' object has no attribute 'disabled' error
        for field_name in db_fields:
            # print("Setting {} to False".format(field_name))
            self.fields[field_name].required = False

    class Meta:
        model = Module3
        fields = db_fields