from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from django.contrib.auth import logout
from instagram.client import InstagramAPI
from social_django.models import UserSocialAuth
from .models import Vangouser
import Algorithmia
import json

client_secret = settings.SOCIAL_AUTH_INSTAGRAM_SECRET
client = Algorithmia.client("simCAFV0mJtYSMFC7g1kaOv8XGU1")


def logout_view(request):
    logout(request)
    return redirect('/')


class Home(View):
    def get(self, request):
        template_name = 'base.html'
        img = []
        try:
            user = UserSocialAuth.objects.get(user=request.user)
            access_token = user.extra_data['access_token']
            uuid = user.uid
            api = InstagramAPI(access_token=access_token, client_secret=client_secret)
            recent_media, next_ = api.user_recent_media(user_id=uuid, count=7)
            for media in recent_media:
                img.append(media.images['standard_resolution'].url)
        except Exception:
            pass
        ctx = {
            'imgs': img
        }
        return render(request, template_name, ctx)


def modified_photo(request):
    if request.method == 'POST':
        img_url = request.POST.get('img_url')
        input_ = {
            "images": [img_url],
            "savePaths": ["data://lopsan/vango/vangoh.jpg"],
            "filterName": "space_pizza"
        }
        nlp_directory = client.dir("data://lopsan/nlp_directory")
        if nlp_directory.exists() is False:
            nlp_directory.create()
        result = client.algo("deeplearning/DeepFilter/").pipe(input_).result['savePaths'][0]
        img_url = "https://algorithmia.com/v1/data/{}".format(result.split("data://")[1])
        ctx = {
            'img_url': img_url
        }
        return HttpResponse(json.dumps(ctx), content_type="application/json")
