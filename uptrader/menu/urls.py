from django.urls import path
from . import views

"""URL patterns used for rendering and testing sample data."""
app_name = 'menu'

urlpatterns = [
    path('', views.test_view, name='main'),
    path('A/', views.test_view, name='A'),
    path('B/', views.test_view, name='B'),
    path('C/', views.test_view, name='C'),
    path('A1/', views.test_view, name='A1'),
    path('A11/', views.test_view, name='A11'),
    path('A12/', views.test_view, name='A12'),
    path('A2/', views.test_view, name='A2'),
    path('B1/', views.test_view, name='B1'),
    path('B2/', views.test_view, name='B2'),
    path('C1/', views.test_view, name='C1'),
    path('C2/', views.test_view, name='C2'),
    path('avatar/', views.test_view, name='avatar'),
    path('email/', views.test_view, name='email'),
    path('language/', views.test_view, name='language'),
    path('settings/', views.test_view, name='settings'),
]
