# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Module3 as Module, Module3Form as ModuleForm
from module2.models import Module2 as Module2


from decisions.decorator import active_user_required
from decisions.views import load_json, load_module, base_restart
from decisions.utils import CheetahSheet, Nylah, ViewHelper

import json

cheetah_sheet1 = CheetahSheet()
cheetah_sheet1.num = 1
cheetah_sheet1.title = "Absolute Targets"

cheetah_sheet2 = CheetahSheet()
cheetah_sheet2.num = 2
cheetah_sheet2.title = "Navigating Numbers"

cheetah_sheet2_2 = CheetahSheet()
cheetah_sheet2_2.num = 2
cheetah_sheet2_2.title = "Absolute Data Quality"

cheetah_sheet3 = CheetahSheet()
cheetah_sheet3.num = 3
cheetah_sheet3.title = "The Story of Your Target's Website"

cheetah_sheet3_2 = CheetahSheet()
cheetah_sheet3_2.num = 3
cheetah_sheet3_2.title = "Absolute Website Data Quality"

cheetah_sheet4 = CheetahSheet()
cheetah_sheet4.num = 4
cheetah_sheet4.title = "Relative: Map vs Terrain"

nylah = Nylah()

# Create your views here.
def navigation():
    """
    Ordered list of URLs for this Module
    """
    urls = [
        reverse('module3_intro'),
        reverse('module3_area'),
        reverse('module3_feeling'),
        reverse('module3_ddd_1'),
        reverse('module3_ddd_2'),
        reverse('module3_ddd_3'),
        reverse('module3_ddd_4'),
        reverse('module3_ddd_5'),
        reverse('module3_ddd_6'),
        reverse('module3_ddd_7'),
        reverse('module3_ddd_8'),
        reverse('module3_ddd_explain'),
        reverse('module3_ddd_defined'),
        reverse('module3_success_terms'),
        reverse('module3_vision'),
        reverse('module3_game1_instructions'),
        reverse('module3_game1_game'),
        reverse('module3_game1_results'),
        reverse('module3_cheetah1_intro'),
        reverse('module3_cheetah1_sheet'),
        reverse('module3_cheetah2_sheet'),
        reverse('module3_cheetah2_sheet2'),
        reverse('module3_cheetah3_sheet'),
        reverse('module3_cheetah3_sheet2'),
        reverse('module3_sum_up'),
        reverse('module3_cheetah4_intro'),
        reverse('module3_cheetah4_sheet'),
        reverse('module3_cheetah4_sheet2'),

    ]

    return urls


"""
Default Page Controller
"""
@active_user_required
def generic_page_controller(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        return save_form(request, module, parsed)

    return render_page(request, module, parsed, {})


"""
Default Render Page Handler
"""
def render_page(request, module, parsed, context={}):
    context['module'] = module
    context['nav'] = parsed
    context['sample_student'] = nylah

    return render(request, parsed['templatePath'], context)


"""
Default Form Save Handler
"""
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

"""
Module Specific Controllers
"""
@active_user_required
def cheetah1_sheet(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.at = json.dumps(request.POST.getlist('at[]'))
        return save_form(request, module, parsed)

    context = {
        'at': ViewHelper.load_json(module.at),
        'cc': ViewHelper.load_json(module.cc),
        'cheetah_sheet': cheetah_sheet1,
        'vs': ViewHelper.load_json(module.vs),
    }
    return render_page(request, module, parsed, context)


@active_user_required
def cheetah2_sheet(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        return save_form(request, module, parsed)

    context = {
        'cheetah_sheet': cheetah_sheet2,
    }
    return render_page(request, module, parsed, context)

@active_user_required
def cheetah2_sheet2(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.at2 = json.dumps(request.POST.getlist('at2[]'))
        return save_form(request, module, parsed)

    context = {
        'at2': ViewHelper.load_json(module.at2),
        'at2_most': module.at2_most,
        'at_numbers': Module.get_at2_numbers(),
        'cheetah_sheet': cheetah_sheet2_2,
    }
    return render_page(request, module, parsed, context)


@active_user_required
def cheetah3_sheet(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        return save_form(request, module, parsed)

    context = {
        'cheetah_sheet': cheetah_sheet3,
    }
    return render_page(request, module, parsed, context)

@active_user_required
def cheetah3_sheet2(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.at3 = json.dumps(request.POST.getlist('at3[]'))
        return save_form(request, module, parsed)

    context = {
        'at3': ViewHelper.load_json(module.at3),
        'at3_most': module.at3_most,
        'at_numbers': Module.get_at3_numbers(),
        'cheetah_sheet': cheetah_sheet3_2,
    }
    return render_page(request, module, parsed, context)

@active_user_required
def cheetah4_intro(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        return save_form(request, module, parsed)

    context = {
        'cheetah_sheet': cheetah_sheet4,
    }
    return render_page(request, module, parsed, context)

@active_user_required
def cheetah4_sheet(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.at4 = json.dumps(request.POST.getlist('at4[]'))
        return save_form(request, module, parsed)

    context = {
        'at4': ViewHelper.load_json(module.at4),
        'at_numbers': Module.get_at4_numbers(),
        'cheetah_sheet': cheetah_sheet4,
    }
    return render_page(request, module, parsed, context)


@active_user_required
def cheetah4_sheet2(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        return save_form(request, module, parsed)

    at4 = ViewHelper.load_json(module.at4)
    yes = 0

    at_numbers = Module.get_at4_numbers()
    total = len(at_numbers)

    for ans in at4:
        yes += 1
    no = total - yes

    # Mixed
    if yes == no:
        results = "mixed"
    # If mostly yes,
    elif yes > no:
        results = "yes"
    # If mostly no
    else:
        results = "no"

    context = {
        'cheetah_sheet': cheetah_sheet4,
        'results': results,
    }
    return render_page(request, module, parsed, context)


@active_user_required
def ddd(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    # There is only one template path
    parsed['templatePath'] = 'module3/ddd/1.html'

    ddd_parameters = module.get_ddd_parameters()

    dd_params = {}
    if module.dd_params:
        dd_params = load_json(module.dd_params)

    # What is our current step?
    currentStep = int(parsed['step'])
    # Name of the form field we're saving
    form_name = "ddd_{0}".format(currentStep)
    # Question to display
    question = ddd_parameters[currentStep-1]['question']
    # Slider labels
    labels = ddd_parameters[currentStep-1]['labels']

    if request.method == 'POST':
        if form_name not in dd_params:
            dd_params[form_name] = ""

        dd_params[form_name] = request.POST.get(form_name)

        module.dd_params = json.dumps(dd_params)
        return save_form(request, module, parsed)

    # Show a different text blob based on their feeling
    if module.feeling_start != 5:
        feeling_bad = True
    else:
        feeling_bad = False

    # Did we answer this already?
    current_answer = 1
    if form_name in dd_params:
        current_answer = dd_params[form_name]
        if current_answer is None:
            current_answer = 1

    context = {
        'current_answer': current_answer,
        'feeling_bad': feeling_bad,
        'form_name': form_name,
        'labels': labels,
        'question': question,
    }
    return render_page(request, module, parsed, context)


@active_user_required
def ddd_explain(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    ddd_parameters = module.get_ddd_parameters()

    total = 0
    print(module.dd_params)
    if module.dd_params:
        answers = load_json(module.dd_params)
        for form_name in answers:
            total += int(answers[form_name])

    context = {
        'ddd_parameters': ddd_parameters,
        'dd_answers': module.dd_params,
        'total': total,
    }
    return render_page(request, module, parsed, context)


@active_user_required
def feeling_start(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        return save_form(request, module, parsed)

    feeling_start = module.feeling_start
    if feeling_start is None:
        feeling_start = 1
    if feeling_start == "":
        feeling_start = 1

    context = {
        'feeling_start': feeling_start,
    }
    return render_page(request, module, parsed, context)


@active_user_required
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
        return redirect(reverse('module3_game1_results'))
        #return redirect(parsed['nextUrl'])
    else:
        ViewHelper.clear_game_answers(module)

    context = {
        'num_questions': len(game_questions),
        'questions': game_questions.values(),
    }

    return render_page(request, module, parsed, context)

@active_user_required
def game1_results(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.br = json.dumps(request.POST.getlist('br[]'))
        return save_form(request, module, parsed)

    bias_results = []
    biases = load_json(module.biases)

    bias_definitions = Module2.get_biases()
    for key,value in biases.items():
        # Return the top two biases
        if len(bias_results) >= 2:
            break

        # Find the label and definition
        for definition in bias_definitions:
            if definition['key'] == key:
                # Get the label and definition
                bias_results.append({
                    'key': key,
                    'label': definition['label'],
                    'definition': definition['definition']
                })
                break

    print("Total bias results")
    print(bias_results)
    print(parsed)

    context = {
        'answers': module.answers_json,
        'biases': bias_results,
        'br': ViewHelper.load_json(module.br),
        'questions': module.get_game_questions(),
    }

    return render_page(request, module, parsed, context)


@active_user_required
def success_terms(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.success_terms = json.dumps(request.POST.getlist('success_terms[]'))
        return save_form(request, module, parsed)

    context = {
        'success_terms': ViewHelper.load_json(module.success_terms),
    }
    return render_page(request, module, parsed, context)


@active_user_required
def sum_up(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    sorted_sum_up = calculate_sum_up(module)
    # Get the last value color
    selected_color = sorted_sum_up[-1][1]

    context = {
        'at_results': selected_color,
    }
    return render_page(request, module, parsed, context)


@active_user_required
def vision(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.cc = json.dumps(request.POST.getlist('cc[]'))
        module.vs = json.dumps(request.POST.getlist('vs[]'))

        return save_form(request, module, parsed)

    context = {
        'cc': ViewHelper.load_json(module.cc),
        'success_terms': ViewHelper.load_json(module.success_terms),
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

def calculate_sum_up(module):
    # See https://docs.google.com/spreadsheets/d/14oco-rnnKWTQ1SnSdUAQVBZjWnUSNsr08QFYxQpQg-I/edit#gid=0
    scores = {
        'at2': [
            'green',
            'blue',
            'red',
            'green'
        ],
        'at3': [
            'green',
            'red',
            'blue',
            'green'
        ]
    }

    at2 = ViewHelper.load_json(module.at2)
    at3 = ViewHelper.load_json(module.at3)

    # Arrays are zero-based index so deduct 1
    sum_up = {
        'green': 0,
        'red': 0,
        'blue': 0,
    }

    for ans in at2:
        # print(ans)
        ndx = int(ans)-1
        color = scores['at2'][ndx]
        sum_up[color] += 1

    for ans in at3:
        # print(ans)
        ndx = int(ans)-1
        color = scores['at3'][ndx]
        sum_up[color] += 1

    # print(sum_up)
    sorted_sum_up = sorted((value, key) for (key, value) in sum_up.items())

    return sorted_sum_up