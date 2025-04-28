from django.shortcuts import render
from django.urls import resolve
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest


def test_view(request: WSGIRequest) -> HttpResponse:
    """View for page with test data."""
    current_url_name: str = resolve(request.path).url_name
    return render(request, 'menu/test.html', context={'current_page': current_url_name})
