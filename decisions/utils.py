from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

import hashlib
import json
import re

from .models import Course, User
from .parser import parse_request_path

class CheetahSheet:
    def __init__(self):
        self.num = 1
        self.title = 'Bolstering Strengths, Limiting Blind Spots'

    def num(self):
        return self.num

    def title(self):
        return self.title

class ExampleStudent:
    def __init__(self):
        self.name = 'Nylah'
        self.pronoun_subject = 'she'
        self.pronoun_object = 'her'
        self.pronoun_reflexive = 'herself'

    def name(self):
        return self.name

    def pronoun_reflexive(self):
        return self.pronoun_reflexive

    def pronoun_subject(self):
        return self.pronoun_subject

    def pronoun_object(self):
        return self.pronoun_object

class MasterTerm:
    def __init__(self):
        self.master_terms = {
            "Authority Bias": {
                'definition': "The tendency to take on the opinion of someone who is seen as an authority figure",
            },
            "Decision Target": {
                'definition': "The person, place or thing at the center of your decision problem"
            },
            "Liking Bias": {
                'definition': "Gravitating toward things and people we like",
            },
            "Optimism Bias": {
                'definition': "Believing everything will turn out well",
            },
            "Planning Bias": {
                'definition': "Underestimating how long a task will take, even if you've done it before",
            },
            "Projection Bias": {
                'definition': "Putting your own thoughts and desires onto others around you",
            },
            "Relative": {
                'definition': "The R in AREA is for sources that are RELATED to your decision target but not from the Target itself",
            },
            "Social Proof": {
                'definition': "Following the crowd, letting your opinion be influenced by reputation",
            },
        }

    def get_definition(self, key):
        if key in self.master_terms:
            return self.master_terms[key]
        else:
            return { 'definition': "Not defined" }

class Nylah(ExampleStudent):
    # Nylah's first attempt without Critical Concepts
    def without_cc(self):
        return [
            'No, since I want to be able to buy a car',
            'Yes, I like the adventure of going away',
            "I'd go if the school has a great graphic design program",
        ]

    def cc(self):
        return [
            "I'm able to afford it",
            "I want to study graphic design",
            "I still want to help out at home",
        ]

    def cc_as_question(self):
        return [
            {
                'question': "Do I need a car to go college?",
                'explanation': "This answer doesn't get at whether or not Nylah should go away to college",
                'successful': 0,
            },
            {
                'question': "What is the overall cost of the college?",
                'explanation': "It's critical to Nylah to be able to afford college",
                'num': 1,
                'successful': 1,
            },
            {
                'question': "How would my experience at this college differ from everyday life?",
                'explanation': "Any college choice will be different from high school",
                'successful': 0,
            },
            {
                'question': "How is the food in the dorms?",
                'explanation': "This answer doesn't get at whether or not Nylah should go away to college",
                'successful': 0,
            },
            {
                'question': "Does the college have a good graphic design program?",
                'explanation': "It's critical to Nylah that the college supports what she wants to major in",
                'num': 2,
                'successful': 1,
            },
            {
                'question': "Would this choice allow me to help at home?",
                'explanation': "It's critical to Nylah that she provides some help at home ",
                'num': 3,
                'successful': 1,
            },
        ]

class ViewHelper:
    @staticmethod
    def clear_game_answers(module):
        if module.answers:
            module.answers = json.dumps({})
            module.save()

    @staticmethod
    def has_diff(src_str, dst_str):
        hash_a = hashlib.sha256(src_str)
        hash_b = hashlib.sha256(dst_str)

        return (hash_a == hash_b)

    @staticmethod
    def is_mobile(request):
        MOBILE_AGENT_RE = re.compile(r".*(iphone|mobile|androidtouch)", re.IGNORECASE)
        print(request.META['HTTP_USER_AGENT'])

        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            return True

        return False

    @staticmethod
    def load_course(request):
        course = None
        if request.user.is_authenticated():
            courses = Course.objects.filter(user=request.user)
            if courses:
                course = courses.first()
            else:
                course = Course(user=request.user)
                course.save()
        return course

    @staticmethod
    def load_json(json_data):
        json_object = {}
        try:
            json_object = json.loads(json_data)
        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
        return json_object

    @staticmethod
    def load_module(request, step='', Module=None):
        module = None
        course = ViewHelper.load_course(request)
        if course:
            module_list = Module.objects.filter(course=course)
            if module_list:
                module = module_list.first()
                if step:
                    module.step = step
                    #module.save()
                    module.save_without_historical_record()
            else:
                module = Module(course=course, step=step)
                #module.save()
                module.save_without_historical_record()
            module.answers_json = ''
            if module.answers:
                module.answers_json = ViewHelper.load_json(module.answers)
        if not module:
            module = Module()
            if hasattr(module, 'answers_json'):
                module.answers_json = None

        print("Loading Module {0}: {1}".format(module.display_num(), module.name()))
        return module

    @staticmethod
    def parse_request_path(request, module_urls=[]):
        return parse_request_path(request, module_urls)

    @staticmethod
    def send_html_email(to_list, subject, template_name, context, sender=settings.DEFAULT_FROM_EMAIL):
        msg_html = render_to_string(template_name, context)
        msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, bcc=to_list)
        msg.content_subtype = "html"  # Main content is now text/html
        print("In send_html_email before send")
        email_results = msg.send()
        print("In send_html_email after send. results: {}".format(email_results))
        return email_results

    @staticmethod
    def update_view_counter(user=None):
        if user:
            user_list = User.objects.filter(email=user.email)
            if user_list:
                current_user = user_list.first()
                if current_user:
                    print("Updating access_counter {0} for {1} {2}".format(current_user.access_counter,
                                                                           current_user.id, current_user.email))
                    current_user.access_counter = current_user.access_counter + 1
                    current_user.save()
