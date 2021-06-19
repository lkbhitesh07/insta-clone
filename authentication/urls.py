from django.urls import path
from authentication.views import SignUpView, SignInView, SignOutView
#from authentication.views import PrView, PrCView, PrDView, PrCView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

urlpatterns = [
    path('', SignInView.as_view(), name='signin_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('signout/', SignOutView.as_view(), name='signout_view'),
    
    # path('password/reset/', PrView.as_view(), name='password_reset'),#name defined are according to default django.
    # path('password/reset/confirm/<uidb64>/<token>', PrCView.as_view(), name='password_reset_confirm'),
    # path('password/reset/done/', PrDView.as_view(), name='password_reset_done'),
    # path('password/reset/complete/', PrCView.as_view(), name='password_reset_complete'),

    #Method-2 another method from which we can do Password Reset

    path('password/reset/', PasswordResetView.as_view(
        email_template_name = 'authentication/password_reset_email.html', #default values we can change to change the template of email
        template_name = 'authentication/password_reset.html'
    ), name='password_reset'),

    path('password/reset/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        template_name = 'authentication/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('password/reset/done/', PasswordResetDoneView.as_view(
        template_name = 'authentication/password_reset_done.html'
    ), name='password_reset_done'),

    path('password/reset/complete/', PasswordResetCompleteView.as_view(
        template_name = 'authentication/password_reset_complete.html'
    ), name='password_reset_complete'),
]