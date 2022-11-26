from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('user_page/', user_page, name='user'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('sing_in/', LoginUser.as_view(), name='sing_in'),
    path('transfer/', transfer, name='transfer'),
    path('bringing_in/', bringing_in, name='bringing_in'),
    path('logout/', logout_user, name='logout'),
]
