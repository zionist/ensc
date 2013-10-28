from django.db import models


class Page(models.Model):

    class Meta:
        app_label = "core"
        verbose_name = "Page"

    def __unicode__(self):
        return "%s | %s" % (self.header, self.url)

    url = models.CharField('link to page', max_length=200,
                          help_text='link to page')
    header = models.CharField('page header', max_length=400,
                              help_text='page header')
    short_text = models.TextField('short text', help_text='short text')
    detail_text = models.TextField('detail text', blank=True, help_text='detail text')
    title = models.CharField('title', max_length=4096, help_text='page title')
    description = models.TextField('description', blank=True, help_text='description')


class Block(models.Model):

    class Meta:
        app_label = "core"
        verbose_name = "Block"
        ordering = ["-weight"]

    def __unicode__(self):
        return "%s" % (self.header)

    header = models.CharField('block header', max_length=400,
                              help_text='block header')
    text = models.TextField('block text', help_text='block text')
    weight = models.IntegerField('Weight for order', default=0, 
        help_text='Weight for ordering block on page. If value is greater, block will be displayed hier on page')
    pages = models.ManyToManyField(Page, help_text='On which pages this block should be displayed')


class Menu(models.Model):

    class Meta:
        app_label = "core"
        verbose_name = "Menu"
        ordering = ["-weight"]

    def __unicode__(self):
        return "%s" % (self.name)

    name = models.CharField('menu name', max_length=400,
                              help_text='menu name')
    url = models.CharField('menu url', max_length=400,
                              help_text='url to there menu item points')
    weight = models.IntegerField('Weight for order', default=0, 
        help_text='Weight for ordering menu itimes on page. "\
        "If value is greater, menu item will be displayed on the right of the page')
    hidden_phone = models.NullBooleanField("hide this entry in mobile version", 
        help_text="hide this entry in mobile version")
