from django.urls import path
from authentication.views import PrView, SignUpView, SignInView, SignOutView, PrCView, PrDView, PrCView

urlpatterns = [
    path('', SignInView.as_view(), name='signin_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('signout/', SignOutView.as_view(), name='signout_view'),
    path('password/reset/', PrView.as_view(), name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>', PrCView.as_view(), name='password_reset_confirm'),
    path('password/reset/done/', PrDView.as_view(), name='password_reset_done'),
    path('password/reset/complete/', PrCView.as_view(), name='password_reset_complete'),
]