from ensc.core.models import Page, Block, Menu
from django.contrib import admin


class BlockAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', )
    search_fields = ('header', 'text')
    # class Media:
        # js = [
        #    '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        #    '/static/grappelli/tinymce_setup/tinymce_setup.js',
        # ]
        # css = {
        #    'all': ('/static/bootstrap/css/bootstrap.css',)
        # }


class PageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', )
    search_fields = ('header', 'short_text', 'detail_text', )


class MenuAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', )
    search_fields = ('name', )


admin.site.register(Page, PageAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Menu, MenuAdmin)
