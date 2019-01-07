from django.conf.urls import url, include
from django.views.generic import RedirectView

import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='module3_intro', permanent=True)),

    url(r'^intro/?$', views.generic_page_controller, name='module3_intro'),
    url(r'^review/?$', views.review, name='module3_review'),
    url(r'^map/?$', views.show_map, name='module3_map'),

    # Game 1
    url(r'^game1/instructions/?$', views.generic_page_controller, name='module3_game1_instructions'),
    url(r'^game1/game/?$', views.game, name='module3_game1_game'),
    url(r'^game1/results/?$', views.game, name='module3_game1_results'),

    url(r'^summary/?$', views.summary, name='module3_summary'),

    # Other Module-specific URLs
    url(r'^restart/?$', views.restart, name='module3_restart'),
]