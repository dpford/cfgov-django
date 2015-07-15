from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView

from cfgov.views import office, subpage

from sheerlike.views.generic import SheerTemplateView


urlpatterns = [
    url(r'^$', SheerTemplateView.as_view(), name='home'),

    url(r'^blog/', include([
        url(r'^$', TemplateView.as_view(template_name='blog/index.html'),
                   name='index'),
        url(r'^(?P<doc_id>[\w-]+)/$',
                   SheerTemplateView.as_view(doc_type='posts',
                                           local_name='post',
                                           default_template='blog/_single.html',),
                   name='detail'),], namespace='blog')),

    url(r'^newsroom/', include([
        url(r'^$', TemplateView.as_view(template_name='newsroom/index.html'),
                   name='index'),
        url(r'^press-resources/$',
            TemplateView.as_view(template_name='newsroom/press-resources/index.html'),
            name='press-resources'),
        url(r'^(?P<doc_id>[\w-]+)/$',
                   SheerTemplateView.as_view(doc_type='newsroom',
                                           local_name='newsroom',
                                           default_template='newsroom/_single.html',),
                   name='detail'),], namespace='newsroom')),

    url(r'^budget/',include([
        url(r'^$', TemplateView.as_view(template_name='budget/index.html'), name='home'),
        url(r'^(?P<page_slug>[\w-]+)/$',
            SheerTemplateView.as_view(),
            name='page'),
        ], namespace="budget")),

    url(r'^the-bureau/', include([
        url(r'^$', SheerTemplateView.as_view(template_name='the-bureau/index.html'),
            name='index'),
        url(r'^(?P<page_slug>[\w-]+)/$',
            SheerTemplateView.as_view(),
            name='page'),
            ], namespace='the-bureau')),

    url(r'^doing-business-with-us/', include([
        url(r'^$',
            TemplateView.as_view(template_name='doing-business-with-us/index.html'),
            name='index'),
        url(r'^(?P<page_slug>[\w-]+)/$',
            SheerTemplateView.as_view(),
            name='page'),

    ], namespace='business')),

    url(r'^contact-us/', include([
        url(r'^$',
            TemplateView.as_view(template_name='contact-us/index.html'),
            name='index'),

    ], namespace='contact-us')),
    url(r'^offices/', include([
        url(r'^(?P<office_id>[\w-]+)/$', 'cfgov.views.office', name='office'),
        url(r'^(?P<office_id>[\w-]+)/(?P<subpage_id>[\w-]+)/$', 'cfgov.views.subpage', name='sub_page')
                              ], namespace='offices'
        )
    ),
    url(r'^activity-log/$', TemplateView.as_view(template_name='activity-log/index.html'), name='activity-log'),
]

from sheerlike import register_permalink

register_permalink('posts', 'blog:detail')
register_permalink('newsroom', 'newsroom:detail')
