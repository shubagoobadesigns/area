from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime

from .models import Module3 as Module, Module3Form as ModuleForm
from module2.models import Module2 as PreviousModule
from decisions.views import base_restart
from decisions.utils import CheetahSheet, ExampleStudent, ViewHelper

import datetime
import json

cheetah_sheet6 = CheetahSheet()
cheetah_sheet6.num = 6
cheetah_sheet6.title = "Placeholder"

def navigation():
    """
    Ordered list of URLs for this Module
    """
    urls = [
        reverse('module3_intro'),
        reverse('module3_review'),
        reverse('module3_map'),
        reverse('module3_game1_instructions'),
        reverse('module3_game1_game'),
        reverse('module3_game1_results'),
        reverse('module3_summary'),
    ]

    return urls


@login_required
def generic_page_controller(request):
    """
    Default Page Controller
    """
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        return save_form(request, module, parsed)

    return render_page(request, module, parsed, {})


def render_page(request, module, parsed, context={}):
    """
    Default Render Page Handler
    """
    context['module'] = module
    context['nav'] = parsed

    return render(request, parsed['templatePath'], context)


def save_form(request, module, parsed):
    """
    Default Form Save Handler
    """
    form = ModuleForm(request.POST, instance=module)
    if form.is_valid():
        form.save()
        return redirect(parsed['nextUrl'])
    else:
        print("Form on step: {0} did not validate".format(parsed['currentStep']))
        print(form.errors)

@login_required
def restart(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    return base_restart(request, Module, parsed['prefix'])


@login_required
def review(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    context = {
    }

    return render_page(request, module, parsed, context)


@login_required
def show_map(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    context = {
        'display_mode': 'all',
        'btn_label': 'Ready to make better decisions?',
    }
    return render_page(request, module, parsed, context)


@login_required
def summary(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.completed_on = datetime.datetime.now()
        module.save()
        return redirect(reverse('decisions_home'))

    context = {}

    return render_page(request, module, parsed, context)


@login_required
def game(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    # Add title to each question
    game_questions = Module.get_game_questions()
    for title in game_questions.keys():
        game_questions[title]['title'] = title

    if request.method == 'POST':
        answers = {}
        if module.answers:
            answers = ViewHelper.load_json(module.answers)
        for i in range(0, len(game_questions.values())):
            index = str(i)
            question_i = game_questions.values()[i]
            attr_i = request.POST.get('answer[' + index + ']')
            answers[question_i['title']] = attr_i
        module.answers = json.dumps(answers)
        #module.biases = json.dumps(calculate_biases(game_questions, answers))
        module.save()

        #print("Redirecting to: " + parsed['nextUrl'])
        # TODO: figure out why we cannot calculate the nextUrl
        return redirect(reverse('module3_game1_results'))
        #return redirect(parsed['nextUrl'])
    else:
        ViewHelper.clear_game_answers(module)

    context = {
        'num_questions': len(game_questions),
        'questions': game_questions.values(),
    }

    print("num_questions: ")
    print(len(game_questions))

    return render_page(request, module, parsed, context)

"""
Module Specific Utilities
"""
def clear_game_answers(module):
    if module.answers:
        module.answers = json.dumps({})
        module.save()