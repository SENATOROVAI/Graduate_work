from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from market.views import *

app_name='market'
urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('user/register',RegisterAccount.as_view(),name='user-register'),
]
