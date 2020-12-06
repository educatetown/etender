from django.conf import settings
from django.conf.urls.static import static

from .views import ProfileDetailView, ProfileUpdateView
from django.conf.urls import url

app_name = 'profiles'

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', ProfileUpdateView.as_view(), name='update')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
