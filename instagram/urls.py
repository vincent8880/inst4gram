from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^upload/$', views.upload_image, name='upload_image'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
    url(r'^image/(?P<image_id>\d+)', views.single_image, name='single_image'),
    url(r'^search/', views.search, name='search'),
    url(r'^like/(?P<operation>.+)/(?P<pk>\d+)',views.like, name='like'),
    url(r"^profile/update/$", views.update_profile, name = "update_profile"),
    url(r"^accounts/profile/$",views.index, name = 'home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)