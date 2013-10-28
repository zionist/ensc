from core.models import Page, Menu
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

class PageDetailView(DetailView):
    def __init__(self):
        super(PageDetailView, self).__init__()
    model = Page
    template_name = 'page.html'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        context['menu'] = Menu.objects.all().order_by('-weight')
        url = self.request.get_full_path()
        # end of request path
        for item in context['menu']:
            # set active menu tab
            if item.url.split('/')[-1:][0] == url.split('/')[-1:][0]:
                item.active = 'True'
        return context

    def get_queryset(self):
        query_set = super(PageDetailView, self).get_queryset()
        return query_set
