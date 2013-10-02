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
    detail_text = models.TextField('detail text', help_text='detail text')


class Block(models.Model):

    class Meta:
        app_label = "core"
        verbose_name = "Block"

    def __unicode__(self):
        return "%s" % (self.header)

    header = models.CharField('block header', max_length=400,
                              help_text='block header')
    text = models.TextField('block text', help_text='block text')
    pages = models.ManyToManyField(Page)
