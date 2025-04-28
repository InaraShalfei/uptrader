from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='название')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
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
        if self.named_url:
            # try:
                return reverse('menu:'+self.named_url)
            # except NoReverseMatch:
            #     return self.url
        return self.url

    def __str__(self):
        return self.title
