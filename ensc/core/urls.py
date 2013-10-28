from django.conf.urls import patterns, include, url
from core.views import PageDetailView, ContactView

urlpatterns = patterns('',
    url(r'^pages/(?P<slug>\D+)$',  PageDetailView.as_view()),
    url(r'^contact$',  ContactView.as_view()),
)
