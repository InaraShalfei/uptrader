from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    """
        Represents a navigation menu.
        A Menu serves as a container for related MenuItems. Each menu is uniquely
        identified by its name.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name='название')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
        Represents a single item within a navigation menu.
        Each MenuItem may optionally have a parent, allowing the creation
        of hierarchical (tree-like) menu structures.
    """
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', verbose_name='меню')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                               verbose_name='элемент меню')
    title = models.CharField(max_length=100, verbose_name='заголовок')
    url = models.CharField(max_length=200, blank=True, verbose_name='url меню')
    named_url = models.CharField(max_length=200, blank=True, verbose_name='именованный url меню')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def get_url(self):
        """ Returns the resolved URL (named URL if possible, otherwise static URL). """
        if self.named_url:
            try:
                return reverse('menu:' + self.named_url)
            except NoReverseMatch:
                return self.url
        return self.url

    def __str__(self):
        return self.title
