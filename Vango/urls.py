from django.conf.urls import url, include
from django.contrib import admin
from userprofiles.views import Home

urlpatterns = [
    url(r'^$', Home.as_view()),
    url('', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
]
