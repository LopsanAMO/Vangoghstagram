from django.conf.urls import url
from .views import modified_photo


urlpatterns = [
    url(r'^image/', modified_photo)
]
