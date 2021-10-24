from django.urls import path, re_path

from pages import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('consultation/', views.consultation, name='consultation'),
    path('cost/', views.cost, name='cost'),
    path('about/', views.about, name='about'),
    path('abroad/', views.abroad, name='abroad'),
]

