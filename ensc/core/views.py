from core.models import Page
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
        return context

    def get_queryset(self):
        query_set = super(PageDetailView, self).get_queryset()
        return query_set
