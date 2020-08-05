from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

path('', views.persons_list, name='list'),
path('form/', views.fillDetailForm, name='form'),
path('searchList', views.searchResult, name='search'),
path('g_sheet_import', views.g_sheet_import, name='g_sheet_import'),
#url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$',views.step_detail,name = 'step'),
#url(r'(?P<pk>\d+)/$',views.course_detail,name ='detail'),

]