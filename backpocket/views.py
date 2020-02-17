# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Backpocket as Module, BackpocketForm as ModuleForm

from decisions.views import load_json, load_module, base_restart
from decisions.utils import CheetahSheet, ViewHelper

import json

cheetah_sheet1 = CheetahSheet()
cheetah_sheet1.num = 1
cheetah_sheet1.title = "Absolute Targets"

cheetah_sheet2 = CheetahSheet()
cheetah_sheet2.num = 2
cheetah_sheet2.title = "Navigating Numbers"

cheetah_sheet3 = CheetahSheet()
cheetah_sheet3.num = 3
cheetah_sheet3.title = "The Story of Your Target's Website"

# Create your views here.
def navigation():
    """
    Ordered list of URLs for this Module
    """
    urls = [
        reverse('backpocket_intro'),
        reverse('backpocket_area'),
        reverse('backpocket_feeling'),
        reverse('backpocket_decision_problem'),
        reverse('backpocket_explain'),
        reverse('backpocket_ddd'),
        reverse('backpocket_vision'),
        reverse('backpocket_cheetah1_sheet'),
        reverse('backpocket_cheetah2_sheet'),
        reverse('backpocket_cheetah3_sheet'),
        reverse('backpocket_sum_up'),
        reverse('backpocket_relative'),
        reverse('backpocket_relative2'),
        reverse('backpocket_relative3'),

    ]

    return urls


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
        print("Form on step: {0} validated. Redirecting to {1}".format(parsed['currentStep'], parsed['nextUrl']))
        form.save()
        return redirect(parsed['nextUrl'])
    else:
        print("Form on step: {0} did not validate".format(parsed['currentStep']))
        print(form.errors)
        return redirect(parsed['nextUrl'])


def at_results(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    context = {
        'at_results': "green",
    }
    return render_page(request, module, parsed, context)

def at_results(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    context = {
        'at_results': "green",
    }
    return render_page(request, module, parsed, context)


def cheetah1_sheet(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.at = json.dumps(request.POST.getlist('at[]'))
        return save_form(request, module, parsed)

    context = {
        'at': ViewHelper.load_json(module.at),
        'cheetah_sheet': cheetah_sheet1,
    }
    return render_page(request, module, parsed, context)


def cheetah2_sheet(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.at2 = json.dumps(request.POST.getlist('at2[]'))
        return save_form(request, module, parsed)

    context = {
        'at2': ViewHelper.load_json(module.at2),
        'at2_most': module.at2_most,
        'at_numbers': Module.get_at2_numbers(),
        'cheetah_sheet': cheetah_sheet2,
    }
    return render_page(request, module, parsed, context)


def cheetah3_sheet(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.at3 = json.dumps(request.POST.getlist('at3[]'))
        return save_form(request, module, parsed)

    context = {
        'at3': ViewHelper.load_json(module.at3),
        'at3_most': module.at3_most,
        'at_numbers': Module.get_at3_numbers(),
        'cheetah_sheet': cheetah_sheet3,
    }
    return render_page(request, module, parsed, context)


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
            answers = load_json(module.answers)
        for i in range(0, len(game_questions.values())):
            index = str(i)
            question_i = game_questions.values()[i]
            attr_i = request.POST.get('answer[' + index + ']')
            answers[question_i['title']] = attr_i
        module.answers = json.dumps(answers)
        module.biases = json.dumps(calculate_biases(game_questions, answers))
        module.save()

        #print("Redirecting to: " + parsed['nextUrl'])
        # TODO: figure out why we cannot calculate the nextUrl
        return redirect(reverse('backpocket_explain'))
        #return redirect(parsed['nextUrl'])
    else:
        ViewHelper.clear_game_answers(module)

    context = {
        'num_questions': len(game_questions),
        'questions': game_questions.values(),
    }

    return render_page(request, module, parsed, context)


def vision(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.cc = json.dumps(request.POST.getlist('cc[]'))
        module.vs = json.dumps(request.POST.getlist('vs[]'))

        return save_form(request, module, parsed)

    context = {
        'cc': ViewHelper.load_json(module.cc),
        'vs': ViewHelper.load_json(module.vs),
    }
    return render_page(request, module, parsed, context)




def calculate_biases(game_questions, answers):
    """
    Module Specific Utilities
    """
    biases = {}
    for i in range(0, len(game_questions.values())):
        question_i = game_questions.values()[i]
        bias = question_i['bias']
        if bias not in Module.get_biases():
            biases[bias] = {
                'total': 1,
                'biased': 0,
                'ratio': 0,
            }
        else:
            biases[bias]['total'] += 1
        if answers[question_i['title']] == '':
            answers[question_i['title']] = 0  # TODO - shouldn't need it
        if int(answers[question_i['title']]) == int(question_i['bias_answer']):
            biases[bias]['biased'] += 1
        biases[bias]['ratio'] = int(float(biases[bias]['biased']) / float(biases[bias]['total']) * 100)
    return biases
