from django import template

from django.urls import resolve

from ..models import Menu

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path
    current_url_name = resolve(current_path).url_name

    try:
        menu = Menu.objects.prefetch_related('items__children').get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_items': []}

    all_items = list(menu.items.all())

    item_map = {}
    tree = {}

    for item in all_items:
        item_map[item.id] = {
            'item': item,
            'children': [],
            'is_active': False,
            'is_open': False
        }

    for item in all_items:
        if item.parent_id:
            item_map[item.parent_id]['children'].append(item_map[item.id])
        else:
            tree[item.id] = item_map[item.id]

    def mark_active(item_dict):
        item = item_dict['item']
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
