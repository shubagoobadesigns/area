from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

from decisions.models import Course, BaseModule

class Module2(BaseModule):
    answers = models.TextField(default='')
    # Game2 answers
    answers2 = models.TextField(default='')
    biases = models.TextField(default='')
    more_facts = models.TextField(default='')
    nylah_bias = models.CharField(max_length=40, default='')
    opinions = models.TextField(default='')
    opinions_important = models.CharField(max_length=10, default='')
    opinions_reality = models.CharField(max_length=10, default='')
    perspective = models.TextField(default='')
    my_bias = models.TextField(default='')
    my_bias_impact = models.TextField(default='')
    my_bias_remedy = models.TextField(default='')

    evidence0 = models.CharField(max_length=255, default='')
    evidence1 = models.CharField(max_length=255, default='')
    evidence2 = models.CharField(max_length=255, default='')
    fact0 = models.CharField(max_length=255, default='')
    source0 = models.CharField(max_length=255, default='')
    bias0 = models.CharField(max_length=255, default='')
    fact1 = models.CharField(max_length=255, default='')
    source1 = models.CharField(max_length=255, default='')
    bias1 = models.CharField(max_length=255, default='')
    fact2 = models.CharField(max_length=255, default='')
    source2 = models.CharField(max_length=255, default='')
    bias2 = models.CharField(max_length=255, default='')

    @staticmethod
    def num():
        return 2

    def save_without_historical_record(self, *args, **kwargs):
        #self.skip_history_when_saving = True
        #try:
        ret = self.save(*args, **kwargs)
        #finally:
            #del self.skip_history_when_saving
        return ret

    # Used to display the number to the user
    # internally it's still module 0
    @staticmethod
    def display_num():
        return 3

    @staticmethod
    def name():
        return 'Introduction to Mental Shortcuts'

    @staticmethod
    def get_eval_questions():
        eval_questions = [
            {
                'question': 'Do you feel confident that you know how to solve complex problems?',
                'min': 'Low Confidence',
                'max': 'Very Confident',
            },
            {
                'question': 'How often do you regret or second guess your decisions?',
                'min': 'Rarely',
                'max': 'Always',
            },
            {
                'question': 'Do you feel that you can stop yourself from rushing to judgement or jumping to conclusions?',
                'min': 'No',
                'max': 'Yes, all the time',
            },
            {
                'question': 'How often do you check your assumptions with data?',
                'min': 'Never',
                'max': 'All of the time',
            },
            {
                'question': 'Do you feel well-equipped to gather facts and evidence to help you make your decisions?',
                'min': 'Not Equipped',
                'max': 'Equipped',
            },
            {
                'question': 'How often do you check your assumptions with data?',
                'min': 'Never',
                'max': 'Always',
            },
            {
                'question': 'Do you feel well equipped to try to see the decisions through the eyes of other people impacted by the decision?',
                'min': 'Not Equipped',
                'max': 'Well Equipped',
            },
            {
                'question': 'Overall how would you rate yourself a decision maker?',
                'min': 'Below Average',
                'max': 'Above Average',
            },
        ]

        return eval_questions

    @staticmethod
    def get_biases():
        biases = [
            {
                'key': 'authority',
                'label': 'Authority Bias',
                'action': 'This bias is less likely but might be at work if an authority figure in your life is favorable towards Ohio State.',
                'definition': 'The tendency to take on the opinion of someone who is seen as an authority figure',
                'cheetah4': 'Might you be impacted by an authority figure?',
            },
            {
                'key': 'liking',
                'label': 'Liking Bias',
                'action': 'This bias might be at work if you know someone who also likes it.',
                'definition': 'Gravitating toward things and people we like',
                'cheetah4': 'Are you gravitating toward things and people you like?',
            },
            {
                'key': 'planning',
                'label': 'Planning Bias',
                'action': 'This bias is not relevant because it is about underestimating how long a task will take even if we have done it before.',
                'definition': "Underestimating how long a task will take, even if you've done it before",
                'cheetah4': 'Might you be making an assumption about the time to complete a task?',
            },
            {
                'key': 'optimism',
                'label': 'Optimism Bias',
                'action': "This bias about being overly optimistic isn't at work here.",
                'definition': "Believing everything will turn out well",
                'cheetah4': 'Might you be too optimistic?',
            },
            {
                'key': 'social',
                'label': 'Social Proof',
                'action': 'This bias is most relevant, because it is about being influenced by popularity.',
                'definition': 'Following the crowd, letting your opinion be influenced by reputation',
                'cheetah4': 'Might you be swayed by the crowd?',
            },
            {
                'key': 'projection',
                'label': 'Projection Bias',
                'action': 'This bias is not relevant because it is about projecting your own thoughts and feelings onto others.',
                'definition': 'Putting your own thoughts and desires onto others around you',
                'projection': 'Might you be assuming others agree with your opinion?',
            },
        ]

        return biases

    @staticmethod
    def get_bias_remedies():
        remedies = [
            {
                'key': 'Be more conscious and aware of your actions',
                'comment': 'Yes! Pay close attention to whether you do things like make a full stop at stop signs, or need to hit the brake hard when you approach a red light',
            },
            {
                'key': 'Question your actions by asking yourself whether you might be relying upon assumptions',
                'comment': 'Yes! Consider whether you might be overconfident',
            },
            {
                'key': 'Check assumptions by searching for evidence that may back them up or refute them',
                'comment': 'Yes! You could search the Net for how often new drivers had accidents',
            },
            {
                'key': 'Ask others who know you well to help you evaluate your thinking',
                'comment': "Yes! Ask how's my driving?",
            },
            {
                'key': 'Ask yourself how someone else who you respect might approach the same situation you are in so you push yourself out of your own perspective',
                'comment': 'Yes! Ask someone what they did to make sure they drove safely after getting their license'

            }
        ]

        return remedies

    @staticmethod
    def get_bias_authority_questions():
        bias_authority_questions = {
            'authority1': {
                'question': 'Your mom tells you that you should take a photograph of your credit card in case you lose it. You take out your phone and snap a picture of it and send her a copy to keep.',
                'answer0': 'Correct! Your mom is an authority figure.',
                'answer1': 'No! Are you sure? Check again.',
                'bias': 'authority',
                'bias_answer': 0,
            },
            'authority2': {
                'question': 'Your coach says you should just apply to safety schools and you follow his advice without question.',
                'answer0': 'Correct! Your coach is an authority figure.',
                'answer1': 'No! Are you sure? Check again.',
                'bias': 'authority',
                'bias_answer': 0,
            },
            'authority3': {
                'question': 'Your friend tells you she wants your notes for Spanish and you share them with her',
                'answer0': 'No! Are you sure? Check again.',
                'answer1': 'Correct! Your friend is not an authority figure.',
                'bias': 'authority',
                'bias_answer': 1,
            },
        }

        return bias_authority_questions

    @staticmethod
    def get_bias_remedy_questions():
        bias_remedy_questions = {
            'remedy1': {
                'question': 'Be more conscious and aware of your actions',
                'answer0': 'Yes! Close attention breeds insight.',
                'answer1': 'No! Do you use the radio or your phone? Both are distracting.',
                'bias': 'remedy',
                'bias_answer': 0,
            },
            'remedy2': {
                'question': 'Check for facts',
                'answer0': 'Yes! Find answers about new driver accidents.',
                'answer1': 'No! Really? Knowledge is power',
                'bias': 'remedy',
                'bias_answer': 0,
            },
            'remedy3': {
                'question': 'Get a second opinion',
                'answer0': 'Yes! Learn from others how they stayed safe as new drivers.',
                'answer1': 'No! Really? A second opinion may refined or change your thinking.',
                'bias': 'remedy',
                'bias_answer': 0,
            },
            'remedy4': {
                'question': 'Get feedback on your strengths and blind spots',
                'answer0': 'Yes! Who knows your blind spots?',
                'answer1': 'No! Someone who knows you well may provide insight to improve your decision-making.',
                'bias': 'remedy',
                'bias_answer': 0,
            },
        }

        return bias_remedy_questions

    @staticmethod
    def get_mental_shortcuts(self):
        shortcuts = {
            'liking2': {
               'question': 'When you go down the cereal aisle, do you...',
               'answer0': 'Automatically look for the cereal you want',
               'answer1': 'Look at all of the cereal boxes',
               'bias': 'liking',
               'bias_answer': 0,
            },
            'planning1': {
                'question': 'You have a lab report due in two days. You\'ve done them before so you...',
                'answer0': 'Look at the directions when you start to do it',
                'answer1': 'Read the directions now because each lab is a different experiment',
                'bias': 'planning',
                'bias_answer': 0,
            },
            'optimism1': {
                'question': 'If you just passed your driver\'s license test, do you...',
                'answer0': 'Believe you are an above average driver',
                'answer1': 'Think that\'s silly, how could you be?',
                'bias': 'optimism',
                'bias_answer': 0,
            },
        }

        return shortcuts

    @staticmethod
    def get_sample_student_cheetah_data():
        cheetah_data = [
            {
                'cc': "It has a good graphic design program.",
                'facts': "I gathered facts from the colleges' websites about their graphic design programs. Ohio State has a major and Bates doesn't.",
                'source': "I got the data I needed directly from searching for graphic design on the colleges' websites.",
                'bias': "I checked my assumptions and am glad I did. Bates doesn't have a program so I won't apply there.",
            },
            {
                'cc': "I'm able to afford it.",
                'facts': "I don't have facts. My parents say I can choose the college I want to attend.",
                'source': "I could find facts by searching for tuition facts from all of my college choices. I could also download financial aid forms from the college websites and discuss the facts and forms with my parents.",
                'bias': "The Authority Bias might be at work because my parents are authority figures.",
            },
            {
                'cc': "My family supports my decision.",
                'facts': "My facts come from my observation that my family is helping me with my college search.",
                'source': "I don't think I need more facts.",
                'bias': "I am assuming their support is genuine (even though they will miss me). Social Proof could be at work. They might be doing what they think is best for me. ",
            }
        ]

        return cheetah_data

    @staticmethod
    def get_game_questions():
        game_questions = {
            'authority1': {
                'question': 'When your mom asks you to do something do you...',
                'answer0': 'Do it automatically',
                'answer1': 'Question it first',
                'bias': 'authority',
                'bias_answer': 0,
            },
            'liking1': {
                'question': 'When you saw how good your friend looked with her new short haircut do you ...',
                'answer0': 'Decide to cut your hair the same way',
                'answer1': 'Keep your own haircut style',
                'bias': 'liking',
                'bias_answer': 0,
            },
            'liking2': {
                'question': 'When you go down the cereal aisle, do you...',
                'answer0': 'Automatically look for the cereal you want',
                'answer1': 'Look at all of the cereal boxes',
                'bias': 'liking',
                'bias_answer': 0,
            },
            'planning1': {
                'question': 'You have a lab report due in two days. You know you only got partial credit when you didn\'t write in full sentences, do you...',
                'answer0': 'Look at the directions when you start to do it',
                'answer1': 'Read the directions now because each lab is a different experiment',
                'bias': 'planning',
                'bias_answer': 0,
            },
            'planning2': {
                'question': 'When you look at your homework list, do you...',
                'answer0': 'Start at the top and work on assignments until they are complete or you run out of time',
                'answer1': 'Go over the entire list and plan your time',
                'bias': 'planning',
                'bias_answer': 0,
            },
            'optimism1': {
                'question': 'If you just passed your driver\'s license test, do you...',
                'answer0': 'Believe you are an above average driver',
                'answer1': 'Think that\'s silly, how could you be?',
                'bias': 'optimism',
                'bias_answer': 0,
            },
            'social1': {
                'question': 'At school all of your friends are wearing a popular new brand of sneakers. Do you...',
                'answer0': 'Save up for your own pair, too',
                'answer1': 'Stick with your regular shoes, they\'re fine',
                'bias': 'social',
                'bias_answer': 0,
            },
            'social2': {
                'question': 'You overheard some kids are sneaking alcohol into a party you\'re going to. Do you...',
                'answer0': 'Drink some, because it\'s easier to go along',
                'answer1': 'Going along with the crowd isn\'t a factor in your decision',
                'bias': 'social',
                'bias_answer': 0,
            },
            'projection1': {
                'question': 'You see tickets for your favorite band playing a show nearby. Do you...',
                'answer0': 'Buy two tickets, of course your friend will want to come',
                'answer1': 'Ask your friend before commiting her to buying them',
                'bias': 'projection',
                'bias_answer': 0,
            },
            'planning3': {
                'question': 'You have a big math test in two days. Do you...',
                'answer0': 'Start studying tonight so you have time to ask for help tomorrow',
                'answer1': 'Figure starting tomorrow will be enough time to prepare',
                'bias': 'planning',
                'bias_answer': 0,
            },
            'authority2': {
                'question': 'Your aunt says you should just apply to safety schools. Do you...',
                'answer0': 'Follow her advice without questioning it',
                'answer1': 'Check with your guidance counselor',
                'bias': 'authority',
                'bias_answer': 0,
            },
            'projection2': {
                'question': 'You\'re school changes the dress code without warning. Do you...',
                'answer0': 'You think it\'s unfair and assume your friends do too',
                'answer1': 'You ask around to see how other people feel about the new rule',
                'bias': 'projection',
                'bias_answer': 1,
            },
            'optimism2': {
                'question': 'The weather forecast says rain but the sky is blue so you...',
                'answer0': 'Bring an umbrella',
                'answer1': 'Ignore the forecast',
                'bias': 'optimism',
                'bias_answer': 1,
            },
        }

        return game_questions

    @staticmethod
    def get_game2_questions():
        biases = Module2.get_biases()

        game2_questions = [
            {
                'question': 'Which of these statements IS representative of Authority Bias?',
                'answer0': 'Your friend tells you she wants your notes for Spanish and you share them with her',
                'answer1': 'Your mom tells you that you should take a photograph of your credit card in case you lose it. You take out your phone and snap a picture of it and send her a copy to keep',
                'bias': 'authority',
                'bias_answer': 1,
                'explanation0': 'TRY AGAIN! Your friend is not an authority figure',
                'explanation1': 'Yes your mom is an authority figure',
                'definition': 'Authority Bias: ' + biases[0]['definition'],
                'title': 'authority1',
            },
            {
                'question': "Which of these statements DOESN'T represent Authority Bias?",
                'answer0': 'Your coach says you should just apply to safety schools and you follow his advice without question',
                'answer1': 'On Facebook you see a video about not eating meat and you decide to be a vegetarian',
                'bias': 'authority',
                'bias_answer': 1,
                'explanation0': 'TRY AGAIN! Your coach is an authority figure',
                'explanation1': 'Facebook is not an authority',
                'definition': 'Authority Bias: ' + biases[0]['definition'],
                'title': 'authority2',
            },
            {
                'question': 'Which of these statements IS representative of Liking Bias?',
                'answer0': "When you saw how good your friend looked with her new short haircut you decided to get yours cut the same way.",
                'answer1': "When Apple removed the home button on its latest phones you criticized the move even though you love their products.",
                'bias': 'liking',
                'bias_answer': 0,
                'explanation0': "Yes, your friendship may be coloring your reaction",
                'explanation1': "TRY AGAIN! Your brand loyalty did not cause you to overlook a change you didn't like",
                'definition': 'Liking Bias: ' + biases[1]['definition'],
                'title': 'liking1',
            },
            {
                'question': "Which of these statements DOESN'T represent Liking Bias?",
                'answer0': "You like Apple products, especially the phones, so when Apple removed the home button on its latest phones you justified its move even though you found it annoying.",
                'answer1': "Your shopping for sneakers and you love your Nikes but you still see all the choices offered.",
                'bias': 'liking',
                'bias_answer': 0,
                'explanation0': "TRY AGAIN! Your brand loyalty made you justify a change you didn't like",
                'explanation1': "No, your bias for Nikes hasn't prevented you from seeing your options.",
                'definition': 'Liking Bias: ' + biases[1]['definition'],
                'title': 'liking2',
            },
            {
                'question': 'Which of these statements IS representative of Planning Bias?',
                'answer0': "You've saved up for a car and buy one without realizing that you also have to pay for car insurance and budget for gas.",
                'answer1': "You have a science project due and you know the last one took forever so you leave plenty of time to do this latest one.",
                'bias': 'planning',
                'bias_answer': 0,
                'explanation0': "Yes, this is an example of not properly estimating the full cost of have a car",
                'explanation1': "TRY AGAIN! You are being thoughtful about planning your time.",
                'definition': 'Planning Bias: ' + biases[2]['definition'],
                'title': 'planning1',
            },
            {
                'question': "Which of these statements DOESN'T represent Planning Bias?",
                'answer0': "You have a big math test in two days and you wait until the night before to begin studying.",
                'answer1': "You know you have a doctor's appointment in an hour and it's a 15 minute drive and you leave 20 minutes early to get there on time.",
                'bias': 'planning',
                'bias_answer': 0,
                'explanation0': "TRY AGAIN! This is an example of poor planning",
                'explanation1': "No, you planned to be on-time",
                'definition': 'Planning Bias: ' + biases[2]['definition'],
                'title': 'planning2',
            },
            {
                'question': 'Which of these statements IS representative of Optimism Bias?',
                'answer0': "Adults tell us about the risks of smoking, but you don't think you'll be negatively affected by it.",
                'answer1': 'You apply for a summer internship and are nervous about your chances of being accepted',
                'bias': 'optimism',
                'bias_answer': 0,
                'explanation0': "Yes, it is optimistic to think the risks don't apply",
                'explanation1': 'TRY AGAIN! This worry reflects the uncertainty of the situation',
                'definition': 'Optimism Bias: ' + biases[3]['definition'],
                'title': 'optimism1',
            },
            {
                'question': "Which of these statements DOESN'T represent Optimism Bias?",
                'answer0': "When the fire alarm goes off you assume it is a false alarm.",
                'answer1': "The weather forecast calls for rain even though it's sunny outside but you toss an umbrella in your backpack anyway",
                'bias': 'optimism',
                'bias_answer': 0,
                'explanation0': "TRY AGAIN! This is being optimistic",
                'explanation1': "No, you don't want to be unrealistic",
                'definition': 'Optimism Bias: ' + biases[3]['definition'],
                'title': 'optimism2',
            },
            {
                'question': 'Which of these statements IS representative of Social Proof Bias?',
                'answer0': "At school all of your friends are wearing a popular new brand of sneakers. You need to get them too.",
                'answer1': "Your favorite basketball player started endorsing sneakers that don't fit you well and so the ad has no impact on you",
                'bias': 'social',
                'bias_answer': 0,
                'explanation0': "Yes, this is an example of being socially influenced",
                'explanation1': 'TRY AGAIN! You are adapting your behavior based on what the player doing',
                'definition': 'Social Proof Bias: ' + biases[4]['definition'],
                'title': 'social1',
            },
            {
                'question': "Which of these statements DOESN'T represent Social Proof Bias?",
                'answer0': "You overheard some kids are sneaking alcohol into a party you're going to and you decide to go along with it.",
                'answer1': "A new Avenger movie is out but it got poor reviews. You don't care because you've liked the other Avenger flicks.",
                'bias': 'social',
                'bias_answer': 0,
                'explanation0': "TRY AGAIN! You are adapting your behavior to what others are doing",
                'explanation1': "No, you aren't swayed by others opinions",
                'definition': 'Social Proof Bias: ' + biases[4]['definition'],
                'title': 'social2',
            },
            {
                'question': 'Which of these statements is representative of Projection Bias?',
                'answer0': "You think the quiz in history class is going to be easy but you ask your friend if she's worried.",
                'answer1': "You see tickets for your favorite band playing a show nearby. You get tickets for you and a friend.",
                'bias': 'projection',
                'bias_answer': 1,
                'explanation0': "TRY AGAIN! You are not overestimating that your friend agrees with you",
                'explanation1': 'Yes you are projecting your opinion onto someone else',
                'definition': 'Projection Bias: ' + biases[5]['definition'],
                'title': 'projection1',
            },
            {
                'question': "Which of these statements DOESN'T represent Projection Bias?",
                'answer0': "You're school changes the dress code without warning. You think it's unfair and you assume your friends do too.",
                'answer1': "You think it's important to vote but you don't want to assume your friends do.",
                'bias': 'projection',
                'bias_answer': 1,
                'explanation0': "TRY AGAIN! You're projecting your views onto others",
                'explanation1': "No, you are being careful not to project your opinion onto your friends",
                'definition': 'Projection Bias: ' + biases[5]['definition'],
                'title': 'projection2',
            },
        ]

        return game2_questions


    def get_more_facts(self):
        more_facts = [
            'The student to teacher ratio',
            'Graduation rates',
            'Tuition',
            'Housing',
            'Average SAT/ACT Scores',
            'Financial Aid',
        ]

        return more_facts

    def get_opinions(self):
        opinions = [
            'The weather is in Ohio and Maine',
            'How interesting the classes are',
            'Whether the professors are good',
            'How hard it is to get into classes',
            'How nice the dorms are',
            'How the food is',
            'How much homework there is',
            'Is there a Greek life',
        ]

        return opinions

    def get_perspective(self):
        perspective = [
            'Allows you to learn someone/something\'s story in their own words',
            'Promotes empathy',
            'Promotes understanding',
            'Builds your Self Awareness',
            'Focuses on what motivates the person/organization',
        ]

        return perspective

    @staticmethod
    def pins():
        pins = [
            'Mental Shortcuts',
            'Common Biases',
            'Bias Remedies',
        ]

        return pins

    def __str__(self):
        to_return = "Module 2 step " + self.step
        if self.completed_on:
            to_return = to_return + " completed on " + str(self.completed_on)
        return to_return

    class Meta:
        verbose_name = 'Module 2 Data'
        verbose_name_plural = 'Module 2 Data'

class Module2Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Module2Form, self).__init__(*args, **kwargs)
        # Not all fields are available all at once so set these to false for now
        self.fields['answers'].required = False
        self.fields['answers2'].required = False
        self.fields['biases'].required = False
        self.fields['more_facts'].required = False
        self.fields['nylah_bias'].required = False
        self.fields['opinions'].required = False
        self.fields['opinions_important'].required = False
        self.fields['opinions_reality'].required = False
        self.fields['perspective'].required = False
        self.fields['my_bias'].required = False
        self.fields['my_bias_impact'].required = False
        self.fields['my_bias_remedy'].required = False


    class Meta:
        model = Module2
        fields = ['answers',
                  'answers2',
                  'biases',
                  'more_facts',
                  'my_bias',
                  'my_bias_impact',
                  'my_bias_remedy',
                  'nylah_bias',
                  'opinions',
                  'opinions_important',
                  'opinions_reality',
                  'perspective',
                  ]