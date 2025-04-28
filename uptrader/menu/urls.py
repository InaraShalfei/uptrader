from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('test/', views.test_view, name='main'),
    path('test/A', views.test_view, name='A'),
    path('test/B', views.test_view, name='B'),
    path('test/C', views.test_view, name='C'),
    path('test/A1', views.test_view, name='A1'),
    path('test/A11', views.test_view, name='A11'),
    path('test/A12', views.test_view, name='A12'),
    path('test/A2', views.test_view, name='A2'),
    path('test/B1', views.test_view, name='B1'),
    path('test/B2', views.test_view, name='B2'),
    path('test/C1', views.test_view, name='C1'),
    path('test/C2', views.test_view, name='C2'),
    path('test/avatar', views.test_view, name='avatar'),
    path('test/email', views.test_view, name='email'),
    path('test/language', views.test_view, name='language'),
    path('test/settings', views.test_view, name='settings'),
]
