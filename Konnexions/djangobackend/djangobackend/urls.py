
from django.contrib import admin
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.homepage,name='home_url_name'),
    url(r'^tictactoe/$',views.tictactoe,name='tictactoe_url_name'),
    url(r'^imagegallery/$',views.imagegallery,name='imagegallery_url_name'),
    url(r'^clickcounter/$',views.clickcounter,name='clickcounter_url_name'),
    url(r'^videogalleryform/$',views.videogalleryform,name='videogalleryform_url_name'),
    url(r'^videogallery/$',views.videogallery,name='videogallery_url_name'),
]

urlpatterns += staticfiles_urlpatterns()