from ensc.core.models import Page, Block
from django.contrib import admin


class BlockAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
    search_fields = ('header', 'text')
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]


class PageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
    search_fields = ('header', 'short_text')
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]


admin.site.register(Page, PageAdmin)
admin.site.register(Block, BlockAdmin)
