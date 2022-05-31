from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_view, name='new'),
    path('article/', views.article_view, name='article'),
    path('category/', views.category_view, name='category'),
    path('datail/', views.datail_view, name='datail'),
]