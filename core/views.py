from django.http import request
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView, View
from django.contrib.auth import get_user_model
from core.models import Follow

User = get_user_model()

# Create your views here.
class HomeView(TemplateView):
    template_name = 'core/feed.html'

class FollowDoneView(View):
    def post(self, request, *args, **kwargs):
        followed_user_id = request.POST.get('followed_user_id')
        followed_user_obj = User.objects.get(pk=followed_user_id)

        #we don't want to create same entry of same person following
        try:
            Follow.objects.get(user=request.user, followed=followed_user_obj)
        except Exception as e:
            follow_obj = Follow.objects.create(followed=followed_user_obj)

        return redirect(request.META.get('HTTP_REFERER')) #this will refer to the same page from which the post request came.

class UnFollowDoneView(View):
    def post(self, request, *args, **kwargs):
        unfollowed_user_id = request.POST.get('unfollowed_user_id')
        unfollowed_user_obj = User.objects.get(pk=unfollowed_user_id)

        #we don't want to create same entry of same person following
        try:
            follow_obj = Follow.objects.get(user=request.user, followed=unfollowed_user_obj)
            follow_obj.delete()
        except Exception as e:
            pass

        return redirect(request.META.get('HTTP_REFERER'))
