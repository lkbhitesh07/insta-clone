from django.urls import path
from authentication.views import SignUpView, SignInView, SignOutView
from django.contrib.auth.views import (
            PasswordResetView,
            PasswordResetConfirmView,
            PasswordResetDoneView,
            PasswordResetCompleteView,
            )
from authentication.views import PWDchange, PWDchangeDone

# These are all the urls endpoint related to authentication and authorization.
urlpatterns = [
    path('', SignInView.as_view(), name='signin_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('signout/', SignOutView.as_view(), name='signout_view'),

    path('password/reset/', PasswordResetView.as_view(
        email_template_name = 'authentication/password_reset_email.html',
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

    path('password/change/',
        PWDchange.as_view(),
        name='password_change_view'
        ),

    path('password/change/done/',
        PWDchangeDone.as_view(),
        name='password_change_done_view'
        ),
]
