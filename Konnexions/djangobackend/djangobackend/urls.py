
from django.contrib import admin
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^tictactoe/$',views.tictactoe),
    url(r'^imagegallery/$',views.imagegallery),
    url(r'^clickcounter/$',views.clickcounter),
    url(r'^videogalleryform/$',views.videogalleryform),
    url(r'^videogallery/$',views.videogallery),
]

urlpatterns += staticfiles_urlpatterns()