from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import View
from django.http import HttpResponse
from authentication.forms import UserForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

# All of our views for the endpoints.

User = get_user_model()

def home(request):
    return HttpResponse("Home")

class SignInView(View):
    template_name = 'authentication/signin.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_feed_view')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email_username = request.POST.get('email_username')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(username=email_username)
            email = user_obj.email
        except Exception as e:
            email = email_username

        user = authenticate(request, email=email, password=password)

        if user is None:
            messages.error(request, 'Invalid username or password', extra_tags="error")
            return render(request, self.template_name)

        login(request, user)
        messages.success(request, 'Welcome to instagram', extra_tags="success")
        return redirect('home_feed_view')

class SignUpView(View):
    template_name = 'authentication/signup.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_feed_view')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('home_feed_view')

        context = {'form': form}

        return render(request, self.template_name, context = context)

class SignOutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('signin_view')

class PWDchange(PasswordChangeView):
    template_name = 'authentication/password_change.html'
    success_url = reverse_lazy('password_change_done_view')

class PWDchangeDone(PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'
