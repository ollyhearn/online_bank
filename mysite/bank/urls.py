from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('user/', user_page, name='user'),
    path('registration/', registration, name='registration'),
    path('sing_in/', sing_in, name='sing_in'),
    path('transfer/', transfer, name='transfer'),
    path('bringing_in/', bringing_in, name='bringing_in'),

]
