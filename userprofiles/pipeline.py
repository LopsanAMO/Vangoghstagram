#-*- encoding: utf-8 -*-
import sys
from .models import Vangouser


def save_profile(backend, user, response, is_new, details,  *args, **kwargs):
    if backend.name == 'instagram' and is_new:
        try:
            user_profile = Vangouser()
            user_profile.user = user
            user_profile.username = response['data']['username']
            user_profile.profile_picture = response['data']['profile_picture']
            user_profile.followed_by = response['data']['counts']['followed_by']
            user_profile.follows = response['data']['counts']['follows']
            user_profile.media = response['data']['counts']['media']
            user_profile.save()
        except Exception as e:
            print('errror')
            print(e.message)
