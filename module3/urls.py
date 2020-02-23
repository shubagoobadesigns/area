from django.conf.urls import url
from django.views.generic import RedirectView
import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='backpocket_intro', permanent=True)),

    url(r'^intro/?$', views.generic_page_controller, name='backpocket_intro'),
    url(r'^area/?$', views.generic_page_controller, name='backpocket_area'),
    url(r'^feeling/?$', views.feeling_start, name='backpocket_feeling'),
    url(r'^game1/game/?$', views.game, name='backpocket_decision_problem'),
    url(r'^explain/?$', views.generic_page_controller, name='backpocket_explain'),

    url(r'^ddd/1/?$', views.ddd, name='backpocket_ddd_1'),
    url(r'^ddd/2/?$', views.ddd, name='backpocket_ddd_2'),
    url(r'^ddd/3/?$', views.ddd, name='backpocket_ddd_3'),
    url(r'^ddd/4/?$', views.ddd, name='backpocket_ddd_4'),
    url(r'^ddd/5/?$', views.ddd, name='backpocket_ddd_5'),
    url(r'^ddd/6/?$', views.ddd, name='backpocket_ddd_6'),
    url(r'^ddd/7/?$', views.ddd, name='backpocket_ddd_7'),
    url(r'^ddd/8/?$', views.ddd, name='backpocket_ddd_8'),

    url(r'^vision/?$', views.vision, name='backpocket_vision'),
    url(r'^cheetah1/sheet/?$', views.cheetah1_sheet, name='backpocket_cheetah1_sheet'),
    url(r'^cheetah2/sheet/?$', views.cheetah2_sheet, name='backpocket_cheetah2_sheet'),
    url(r'^cheetah3/sheet/?$', views.cheetah3_sheet, name='backpocket_cheetah3_sheet'),
    url(r'^sum_up/?$', views.at_results, name='backpocket_sum_up'),
    url(r'^relative/intro/?$', views.generic_page_controller, name='backpocket_relative'),
    url(r'^relative/understand/?$', views.generic_page_controller, name='backpocket_relative2'),
    url(r'^relative/useful/?$', views.generic_page_controller, name='backpocket_relative3'),

]
