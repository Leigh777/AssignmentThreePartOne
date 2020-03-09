from django.conf.urls import url, include
from . import views
from django.urls import path, re_path

app_name = 'crm'
urlpatterns = [
               path('', views.home, name='home'),
               re_path(r'^home/$', views.home, name='home'),
               path('crochetHook_list', views.crochetHook_list, name='crochetHook_list'),
               path('crochetHook/<int:pk>/edit/', views.crochetHook_edit, name='crochetHook_edit'),
               path('crochetHook/<int:pk>/delete/', views.crochetHook_delete, name='crochetHook_delete'),
               path('yarn_list', views.yarn_list, name='yarn_list'),
               path('yarn/create/', views.yarn_new, name='yarn_new'),
               path('yarn/<int:pk>/edit/', views.yarn_edit, name='yarn_edit'),
               path('yarn/<int:pk>/delete/', views.yarn_delete, name='yarn_delete'),
               path('gift_list', views.gift_list, name='gift_list'),
               path('gift/create/', views.gift_new, name='gift_new'),
               path('gift/<int:pk>/edit/', views.gift_edit, name='gift_edit'),
               path('gift/<int:pk>/delete/', views.gift_delete, name='gift_delete'),
               path('crochetHook/<int:pk>/summary/', views.summary, name='summary'),
]