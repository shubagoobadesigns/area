from django.conf.urls import url, include
import views
urlpatterns = [
    url(r'^$', views.home, name='Home'),
    url(r'^1$', views.home, name='Home'),
    url(r'^decision$', views.decision, name='Decision'),
    url(r'^2$', views.decision, name='Decision'),
    url(r'^rank', views.rank, name='Rank What Matters'),
    url(r'^3$', views.rank, name='Rank What Matters'),
    url(r'^questions', views.questions, name='Questions'),
    url(r'^4$', views.questions, name='Questions'),
    url(r'^archetype$', views.archetype, name='Archetype'),
    url(r'^archetype_info$', views.archetype_info, name='Archetype_Info'),
    url(r'^5$', views.archetype, name='Archetype'),
    url(r'^archetypes$', views.archetypes_list, name='Archetypes'),
    url(r'^cheetah_sheets$', views.cheetah_sheets, name='Cheetah_Sheets'),
    url(r'^cheetah_master$', views.cheetah_master, name='Cheetah_Master'),
    url(r'^action_map$', views.action_map, name='Action_Map'),
    url(r'^summary$', views.summary, name='Summary'),
    url(r'^dd$', views.autocomplete_dd, name='Dream_Director_Autocomplete'),
    url(r'^restart$', views.restart_session, name='Restart'),
]