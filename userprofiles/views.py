from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import logout
from instagram.client import InstagramAPI
from social_django.models import UserSocialAuth

client_secret = settings.SOCIAL_AUTH_INSTAGRAM_SECRET


def logout_view(request):
    logout(request)
    return redirect('/')


class Home(View):
    def get(self, request):
        template_name = 'home.html'
        img = []
        try:
            user = UserSocialAuth.objects.get(user=request.user)
            access_token = user.extra_data['access_token']
            uuid = user.uid
            api = InstagramAPI(access_token=access_token, client_secret=client_secret)
            recent_media, next_ = api.user_recent_media(user_id=uuid, count=10)
            for media in recent_media:
               img.append(media.images['standard_resolution'].url)
            # media = InstagramFeed.get_media(user_name=user_name, count=8)
        except Exception:
            pass
        ctx = {
            'imgs': img
        }
        return render(request, template_name, ctx)
