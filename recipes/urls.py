from django.conf.urls import url

from . import views

urlpatterns = [

url(r'^$', views.RecipeList.as_view(), name='recipes'),
url(r'^ingredients/$', views.IngredientList.as_view(), name='ingredients'),

#    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]