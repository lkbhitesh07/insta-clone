from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import get_user_model
from user.forms import UserEditForm
from django.contrib import messages
from django.db.models import Q

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
            follows_this_user = False
            for follower_user in request.user.follow_follower.all():
                if user == follower_user.followed:
                    follows_this_user = True
            context = {'user' : user, 'follows_this_user': follows_this_user}
            return render(request, self.template_name_anon, context)

class ProfileEditView(View):
    template_name = 'user/profile_edit.html'
    form_class = UserEditForm

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if username != request.user.username:
            return HttpResponse('<h1>This page does not exist</h1>')

        form = self.form_class(instance=request.user) #doing to automatically get the details of logged in user to edit form.
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance = request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Saved your details in a safe place.')
            return redirect('profile_edit_view', request.user.username)

        else:
            for error in form.errors:
                form[error].field.widget.attrs['class'] += ' is-invalid'

            context = {'form':form}
            return render(request, self.template_name, context)

    
class AllProfilesView(View):
    template_name = 'user/all_profiles.html'

    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('query')
        if search_term:
            all_profiles = User.objects.filter(
                Q(username__contains=search_term) | Q(full_name__contains=search_term)
            ).exclude(username=request.user.username)

        else:
            all_profiles = User.objects.none()
        
        context = {'all_profiles': all_profiles}
        return render(request, self.template_name, context)