from django.conf.urls import url
from django.views.generic import RedirectView
import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='backpocket_intro', permanent=True)),

    url(r'^intro/?$', views.generic_page_controller, name='backpocket_intro'),
    url(r'^area/?$', views.generic_page_controller, name='backpocket_area'),
    url(r'^feeling/?$', views.generic_page_controller, name='backpocket_feeling'),
    url(r'^game1/game/?$', views.game, name='backpocket_decision_problem'),
    url(r'^explain/?$', views.generic_page_controller, name='backpocket_explain'),
    url(r'^ddd/?$', views.generic_page_controller, name='backpocket_ddd'),
    url(r'^vision/?$', views.vision, name='backpocket_vision'),
    url(r'^cheetah1/sheet/?$', views.cheetah1_sheet, name='backpocket_cheetah1_sheet'),
    url(r'^cheetah2/sheet/?$', views.cheetah2_sheet, name='backpocket_cheetah2_sheet'),
    url(r'^cheetah3/sheet/?$', views.cheetah3_sheet, name='backpocket_cheetah3_sheet'),
    url(r'^sum_up/?$', views.at_results, name='backpocket_sum_up'),
    url(r'^relative/intro/?$', views.generic_page_controller, name='backpocket_relative'),
    url(r'^relative/understand/?$', views.generic_page_controller, name='backpocket_relative2'),
    url(r'^relative/useful/?$', views.generic_page_controller, name='backpocket_relative3'),

]
