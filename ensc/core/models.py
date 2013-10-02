from django.db import models

# Create your models here.

class Page(models.Model):
    class Meta:
        app_label = "core"
        verbose_name = "Page"

    def __unicode__(self):
        return "%s | %s" % (self.header, self.url)

    url = models.URLField('link to page', max_length=200, help_text='link to page')
    header = models.CharField('page header', max_length=400, help_text='page header')
    human_redable_text = models.TextField('human redable text', help_text='human redable text')
    seo_text = models.TextField('seo text', help_text='seo text')


class Block(models.Model):
    class Meta:
        app_label = "core"
        verbose_name = "Block"

    def __unicode__(self):
        return "%s | %s" % (self.header, self.regexp)

    header = models.CharField('block header', max_length=400, help_text='block header')
    short_text = models.TextField('short text', help_text='short text')
    detail_text = models.TextField('detail text', help_text='detail text')
    page = models.ForeignKey(Page)
