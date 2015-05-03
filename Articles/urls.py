from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^/$', 'Article.views.index'),
                       url(r'^balance/$', 'Article.views.balance'),
                       url(r'^message/$', 'Article.views.Message'),
                       url(r'^message_content/$', 'Article.views.MessageContent'),
                       url(r'^my_works/$', 'Article.views.my_works'),
                       url(r'^my_works//(?P<work_type>[0-9]+)/$', 'Article.views.my_works'),
                       url(r'^password/$', 'Article.views.password'),
                       url(r'^payments/$', 'Article.views.payments'),
                       url(r'^profile/$', 'Article.views.profile'),
                       url(r'^works/$', 'Article.views.works'),
                       url(r'^sorry/$', 'Article.views.sorry'),
                       # url(r'^categories/categories_list/(?P<cid>[0-9]+)/$', 'list.views.categories_list'),
                       )