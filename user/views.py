from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model
from user.forms import UserEditForm

User = get_user_model()

# Create your views here.

class ProfileView(View):
    template_name_auth = 'user/authenticated_profile.html'
    template_name_anon = 'user/anonymous_profile.html'
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('<h1>This page does not exist</h1>')

        if(username == request.user.username):
            context = {'user' : user}
            return render(request, self.template_name_auth, context)

        else:
            context = {'user' : user}
            return render(request, self.template_name_anon, context)

class ProfileEditView(View):
    template_name = 'user/profile_edit.html'
    form_class = UserEditForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass