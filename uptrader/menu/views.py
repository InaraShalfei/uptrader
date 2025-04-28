from django.shortcuts import render
from django.urls import resolve


def test_view(request):
    current_url_name = resolve(request.path).url_name
    return render(request, 'menu/test.html', context={'current_page': current_url_name})
