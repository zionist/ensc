from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View

from core.models import Page, Menu
from core.forms import ContactForm

class ContactView(View):

    def __init__(self):
        super(View, self).__init__()

    def post(self, request):
        page = Page.objects.get(url='contact')
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/core/pages/thanks')
        else:
            print form.errors
            return self.do_render(request, form)

    def get(self, request):
        return self.do_render(request, ContactForm())

    def do_render(self, request, form):
        # hardcode url
        menu = Menu.objects.all().order_by('-weight')
        url = request.get_full_path()
        # end of request path
        for item in menu:
            print item.url
            # set active menu tab
            if item.url.split('/')[-1:][0] == url.split('/')[-1:][0]:
                item.active = 'True'
        page = Page.objects.get(url='contact')
        url = self.request.get_full_path()
        return render(request, 'contact.html', {
            'form': form,
            'page': page,
            'menu': menu,
            'url': url,
        })
