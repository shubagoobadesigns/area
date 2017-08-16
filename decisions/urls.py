from django.conf.urls import url, include
import views
urlpatterns = [
    url(r'^$', views.home, name='Intro'),
    url(r'^tour$', views.tour, name='Tour'),
    url(r'^1$', views.module1, name='Module 1'),
    url(r'^1/instructions$', views.module1instructions, name='Module 1 Instructions'),
    url(r'^1/game$', views.module1game, name='Module 1 Decision Game'),
    url(r'^1/game_results$', views.module1game_results, name='Module 1 Decision Game Results'),
    url(r'^1/explain', views.module1explain, name='Module 1 Explanation'),
    url(r'^1/area', views.module1area, name='Module 1 AREA Method'),
    url(r'^1/video', views.module1video, name='Module 1 Video'),
    url(r'^1/directions', views.module1directions, name='Module 1 Directions'),
    url(r'^1/sample', views.module1sample, name='Module 1 Sample'),
    url(r'^1/deriving_cc', views.module1deriving_cc, name='Module 1 Deriving Critical Concepts'),
    url(r'^1/exploring_cc', views.module1exploring_cc, name='Module 1 Exploring Critical Concepts'),
    url(r'^1/decision', views.module1decision, name='Module 1 Decision'),
    url(r'^1/cheetah', views.module1cheetah, name='Module 1 Cheetah Sheet'),
    url(r'^1/challenge', views.module1challenge, name='Module 1 Challenge'),
    url(r'^1/buddy', views.module1buddy, name='Module 1 Decision Buddy'),
    url(r'^1/commitment', views.module1commitment, name='Module 1 Commitment'),
    url(r'^1/summary', views.module1summary, name='Module 1 Summary'),

    url(r'^2$', views.module2, name='Module 2'),
]