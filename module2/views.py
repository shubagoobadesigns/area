from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime

from .models import Module2 as Module, Module2Form as ModuleForm
from module1.models import Module1 as PreviousModule
from decisions.views import load_json, load_module, base_restart
from decisions.utils import CheetahSheet, ExampleStudent, ViewHelper

from decisions.decorator import active_user_required

import datetime
import json

cheetah_sheet4 = CheetahSheet()
cheetah_sheet4.num = 4
cheetah_sheet4.title = "Bias and Mental Shortcuts"

cheetah_sheet5 = CheetahSheet()
cheetah_sheet5.num = 5
cheetah_sheet5.title = "Bias Remedies"


def navigation():
    """
    Ordered list of URLs for this Module
    """
    urls = [
        reverse('module2_intro'),
        reverse('module2_review'),
        reverse('module2_map'),
        # Pin 1 - Mental Shortcuts
        reverse('module2_game1_instructions'),
        reverse('module2_game1_game'),
        reverse('module2_explain'),
        # Pin 2 - Common Bias
        reverse('module2_bias'),
        reverse('module2_game1_results'),
        reverse('module2_game2_instructions'),
        reverse('module2_game2_game'),
        reverse('module2_game2_results'),
        reverse('module2_cheetah4_intro'),
        reverse('module2_cheetah4_sheet'),
        reverse('module2_bias_shortcuts'),
        reverse('module2_bias_pro_con'),
        # Pin 3 - Bias Remedies
        reverse('module2_bias_remedies'),
        reverse('module2_bias_practice'),
        reverse('module2_cheetah5_sheet'),
        reverse('module2_cheetah5_apply'),
        reverse('module2_summary'),
    ]

    return urls


@active_user_required
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
    context['sample_student'] = ExampleStudent()
    context['biases'] = module.get_biases()

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

@active_user_required
def bias_authority_practice(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    return bias_yesno(request, parsed, module, Module.get_bias_authority_questions())


@active_user_required
def bias_remedies_practice(request):
    """
    Module Specific Controllers
    """
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        return redirect(parsed['nextUrl'])

    context = {
        'questions': Module.get_bias_remedy_questions(),
    }

    return render_page(request, module, parsed, context)


def bias_yesno(request, parsed, module, game_questions):
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
        return redirect(parsed['nextUrl'])
    else:
        ViewHelper.clear_game_answers(module)

    context = {
        'num_questions': len(game_questions),
        'questions': game_questions.values(),
    }

    return render_page(request, module, parsed, context)


@active_user_required
def cheetah4_sheet(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)
    # Used for rendering the previous module contents
    module1 = load_previous_module(request)

    if request.method == 'POST':
        module.my_bias = json.dumps(request.POST.getlist('my_bias[]'))
        module.my_bias_impact = json.dumps(request.POST.getlist('my_bias_impact[]'))
        return save_form(request, module, parsed)

    context = {
        'cc': ViewHelper.load_json(module1.cc),
        'cc_occurred': ViewHelper.load_json(module1.cc_occurred),
        'decision': module1.decision,
        'decision_as_question': module1.decision_as_question,
        'my_bias': ViewHelper.load_json(module.my_bias),
        'my_bias_impact': ViewHelper.load_json(module.my_bias_impact),
        'cheetah_sheet': cheetah_sheet4,
    }
    return render_page(request, module, parsed, context)


@active_user_required
def cheetah5_report(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, 'cheetah5_apply', Module)

    context = {
        'biases_results': ViewHelper.load_json(module.biases),
        'cheetah_sheet': cheetah_sheet4,
        'module': module,
        'my_bias': ViewHelper.load_json(module.my_bias),
        'my_bias_impact': ViewHelper.load_json(module.my_bias_impact),
        'my_bias_remedy': ViewHelper.load_json(module.my_bias_remedy),
        'my_remedy': ViewHelper.load_json(module.my_remedy),
        'nav': parsed,
        'questions': Module.get_game2_questions(),
    }

    if parsed['currentStep'] == 'cheetah5_email':
        data = {}
        if request.user.is_authenticated():
            emails = [request.user.email]
            subject = "AREA Module {0}: Own it: Apply to real life!".format(module.display_num())
            template = 'module2/cheetah5/email.html'

            try:
                results = ViewHelper.send_html_email(emails, subject, template, context)
                msg = "Email sent to {}. [Code {}]".format(request.user.email, results)
            except Exception as e:
                if hasattr(e, 'message'):
                    print("Exception: " + e.message)
                else:
                    print("Exception: " + e)

                msg = "Unable to send email. There was an internal server error. Try again later."
        else:
            msg = "User is not authenticated. Cannot send email."

        data['message'] = msg
        print("Email: {0} to {1}".format(data['message'], request.user.email))
        return JsonResponse(data)

    return render_page(request, module, parsed, context)


@active_user_required
def cheetah5_sheet(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.my_bias_impact = json.dumps(request.POST.getlist('my_bias_impact[]'))
        module.my_bias_remedy = json.dumps(request.POST.getlist('my_bias_remedy[]'))
        module.my_remedy = json.dumps(request.POST.getlist('my_remedy[]'))
        return save_form(request, module, parsed)

    context = {
        'my_bias_impact': ViewHelper.load_json(module.my_bias_impact),
        'my_bias_remedy': ViewHelper.load_json(module.my_bias_remedy),
        'my_remedy': ViewHelper.load_json(module.my_remedy),
        'cheetah_sheet': cheetah_sheet5,
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
        return redirect(reverse('module2_explain'))
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

    context = {
        'answers': module.answers_json,
        'biases_results': load_json(module.biases),
        'questions': module.get_game_questions(),
    }

    return render_page(request, module, parsed, context)


@active_user_required
def game2_game(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    game_questions = Module.get_game2_questions()

    if request.method == 'POST':
        answers = {}
        for i in range(len(game_questions)):
            index = str(i)
            ans = request.POST.get('answer[' + index + ']')
            title = game_questions[i]['title']

            # Store their answers
            answers[title] = ans

        module.answers2 = json.dumps(answers)
        module.save()

        return redirect(parsed['nextUrl'])
    else:
        ViewHelper.clear_game_answers(module)

    context = {
        'biases': Module.get_biases(),
        'display_mode': 'game2',
        'questions': game_questions,
    }

    return render_page(request, module, parsed, context)

@active_user_required
def game2_results(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    # Get the list of questions
    game_questions = Module.get_game2_questions()
    # Get our answers
    answers2 = ViewHelper.load_json(module.answers2)
    # Store our results
    biases = {}

    for i in range(len(game_questions)):
        title = game_questions[i]['title']
        bias = game_questions[i]['bias']
        expected = game_questions[i]['bias_answer']

        # Initialize
        if bias not in biases:
            biases[bias] = {
                'total': 0,
                'biased': 0,
                'ratio': 0,
            }

        biases[bias]['total'] += 1

        # Did we answer it?
        actual = -1
        if title in answers2:
            actual = answers2.get(title)
            if not actual:
                actual = -1
            else:
                actual = int(actual)


        if expected == actual:
            # We answered it correctly
            biases[bias]['biased'] += 1

        # Calculate the 'ratio' e.g. the total correct
        biases[bias]['ratio'] = int(float(biases[bias]['biased']) / float(biases[bias]['total']) * 100)

    print(biases)

    context = {
        'biases_results': biases,
    }

    return render_page(request, module, parsed, context)


@active_user_required
def restart(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    return base_restart(request, Module, parsed['prefix'])


@active_user_required
def review(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)
    # TODO: move to ViewHelper
    module1 = load_previous_module(request)

    context = {
        'decision_buddy': module1.decision_buddy,
    }

    return render_page(request, module, parsed, context)


@active_user_required
def show_map(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    context = {
        'display_mode': 'all',
        'btn_label': 'Ready to make better decisions?',
    }
    return render_page(request, module, parsed, context)


@active_user_required
def summary(request):
    parsed = ViewHelper.parse_request_path(request, navigation())
    module = ViewHelper.load_module(request, parsed['currentStep'], Module)

    if request.method == 'POST':
        module.completed_on = datetime.datetime.now()
        module.save()
        # Increment the access counter
        ViewHelper.update_view_counter(request.user)
        return redirect(reverse('decisions_home'))

    context = {}

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


def load_previous_module(request):
    return load_module(request, PreviousModule)