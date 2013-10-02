from ensc.core.models import Page, Block
from django.contrib import admin


class BlockAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
    search_fields = ('header', 'text')
    # list_filter = ('may_edit', )


#class BlockInline(admin.TabularInline):
#    model = Block


class PageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
    search_fields = ('header', 'short_text')
#    inlines = [BlockInline, ]


admin.site.register(Page, PageAdmin)
admin.site.register(Block, BlockAdmin)
