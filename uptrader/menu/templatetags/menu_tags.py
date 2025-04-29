from typing import Dict

from django import template
from django.core.handlers.wsgi import WSGIRequest
from django.template import RequestContext
from django.urls import resolve

from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context: RequestContext, menu_name: str) -> Dict:
    """
        Renders a tree-structured menu based on the given menu name.

        This inclusion tag retrieves a `Menu` object by its name, builds a nested
        dictionary representing the menu hierarchy, and marks the active and open
        menu items based on the current request path or URL name.

        Args:
            context (RequestContext): The template context, must contain the current HTTP request.
            menu_name (str): The name of the menu to render.

        Returns:
            Dict: A context dictionary with a `menu_items` key containing the nested menu structure
                  to be used in the 'menu/draw_menu.html' template.

        Behavior:
            - If the menu does not exist, returns an empty list of menu items.
            - Marks the currently active menu item based on the request path or named URL.
            - Expands parent items (`is_open=True`) if any of their children are active.
        """
    request: WSGIRequest = context['request']
    current_path: str = request.path
    current_url_name: str = resolve(current_path).url_name

    try:
        menu: Menu = Menu.objects.prefetch_related('items__children').get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_items': []}

    all_items = list(menu.items.all())

    tree: dict = {}

    item_map = {item.id: {'item': item,
                          'children': [],
                          'is_active': False,
                          'is_open': False
                          }
                for item in all_items}

    for item in all_items:
        if item.parent_id:
            item_map[item.parent_id]['children'].append(item_map[item.id])
        else:
            tree[item.id] = item_map[item.id]

    def mark_active(item_dict: dict) -> bool:
        item: MenuItem = item_dict['item']
        if item.get_url() == current_path or item.named_url == current_url_name:
            item_dict['is_active'] = True
            return True
        for child in item_dict['children']:
            if mark_active(child):
                item_dict['is_open'] = True
                return True
        return False

    for node in tree.values():
        mark_active(node)

    return {'menu_items': tree.values()}
