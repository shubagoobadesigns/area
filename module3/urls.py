from django.conf.urls import url
from django.views.generic import RedirectView
import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='module3_intro', permanent=True)),

    url(r'^intro/?$', views.generic_page_controller, name='module3_intro'),
    url(r'^area/?$', views.generic_page_controller, name='module3_area'),
    url(r'^feeling/?$', views.feeling_start, name='module3_feeling'),

    url(r'^ddd/1/?$', views.ddd, name='module3_ddd_1'),
    url(r'^ddd/2/?$', views.ddd, name='module3_ddd_2'),
    url(r'^ddd/3/?$', views.ddd, name='module3_ddd_3'),
    url(r'^ddd/4/?$', views.ddd, name='module3_ddd_4'),
    url(r'^ddd/5/?$', views.ddd, name='module3_ddd_5'),
    url(r'^ddd/6/?$', views.ddd, name='module3_ddd_6'),
    url(r'^ddd/7/?$', views.ddd, name='module3_ddd_7'),
    url(r'^ddd/8/?$', views.ddd, name='module3_ddd_8'),
    url(r'^ddd/explain/?$', views.ddd_explain, name='module3_ddd_explain'),
    url(r'^ddd/defined/?$', views.generic_page_controller, name='module3_ddd_defined'),

    url(r'^success_terms/?$', views.success_terms, name='module3_success_terms'),
    url(r'^vision/?$', views.vision, name='module3_vision'),

    url(r'^game1/instructions/?$', views.generic_page_controller, name='module3_game1_instructions'),
    url(r'^game1/game/?$', views.game, name='module3_game1_game'),
    url(r'^game1/results/?$', views.game1_results, name='module3_game1_results'),

    url(r'^cheetah1/intro/?$', views.generic_page_controller, name='module3_cheetah1_intro'),
    url(r'^cheetah1/sheet/?$', views.cheetah1_sheet, name='module3_cheetah1_sheet'),

    url(r'^cheetah2/sheet/?$', views.cheetah2_sheet, name='module3_cheetah2_sheet'),
    url(r'^cheetah2/sheet2/?$', views.cheetah2_sheet2, name='module3_cheetah2_sheet2'),

    url(r'^cheetah3/sheet/?$', views.cheetah3_sheet, name='module3_cheetah3_sheet'),
    url(r'^cheetah3/sheet2/?$', views.cheetah3_sheet2, name='module3_cheetah3_sheet2'),

    url(r'^sum_up/?$', views.sum_up, name='module3_sum_up'),
    url(r'^cheetah4/intro/?$', views.cheetah4_intro, name='module3_cheetah4_intro'),
    url(r'^cheetah4/sheet/?$', views.cheetah4_sheet, name='module3_cheetah4_sheet'),
    url(r'^cheetah4/sheet2/?$', views.cheetah4_sheet2, name='module3_cheetah4_sheet2'),

    url(r'^cheetah5/intro/?$', views.cheetah5_intro, name='module3_cheetah5_intro'),
    url(r'^cheetah5/sheet/?$', views.cheetah5_sheet, name='module3_cheetah5_sheet'),

    url(r'^cheetah6/sheet/?$', views.cheetah6_sheet, name='module3_cheetah6_sheet'),
    url(r'^cheetah6/sheet2/?$', views.cheetah6_sheet2, name='module3_cheetah6_sheet2'),
    url(r'^cheetah6/sheet3/?$', views.cheetah6_sheet3, name='module3_cheetah6_sheet3'),
    url(r'^cheetah6/sheet4/?$', views.cheetah6_sheet4, name='module3_cheetah6_sheet4'),

    url(r'^pre_mortem/?$', views.pre_mortem, name='module3_pre_mortem'),
    url(r'^conviction/?$', views.conviction, name='module3_conviction'),
]
