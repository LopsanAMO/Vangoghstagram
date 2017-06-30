from django.conf.urls import url, include
from django.contrib import admin
from userprofiles import urls as Userurls
from userprofiles.views import Home, logout_view


urlpatterns = [
    url(r'^$', Home.as_view()),
    url('', include('social_django.urls', namespace='social')),
    url(r'^user/', include(Userurls)),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/', logout_view),
]
