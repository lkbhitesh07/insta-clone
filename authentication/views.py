from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import View
from django.http import HttpResponse
from authentication.forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
# from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

# Create your views here.

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

        user = authenticate(request, email=email, password=password) #authenticate function will tell if it's in our database or not.

        if user is None:
            messages.error(request, 'Invalid username or password', extra_tags="error")
            return render(request, self.template_name)

        login(request, user)# it will directly login the user
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

        return render(request, self.template_name, context)

class SignOutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('signin_view')

# Method-1 to use password reset - Did for my learning purpose

# class PrView(PasswordResetView):
#     email_template_name = 'authentication/password_reset_email.html'      #default values we can change to change the template of email
#     template_name = 'authentication/password_reset.html'

# class PrCView(PasswordResetConfirmView):
#     template_name = 'authentication/password_reset_confirm.html'

# class PrDView(PasswordResetDoneView):
#     template_name = 'authentication/password_reset_done.html' 

#     #This view also passes the form attribute with itself, which means the default one which django have.
#     #you can see it by simply writing {{ form }} at the template file
#     # In template when we create the form it's important to have the 'name' part same as the django form which is passing by this view otherwise it will not validate
#     # and will not work

# class PrCView(PasswordResetCompleteView):
#     template_name = 'authentication/password_reset_complete.html'
