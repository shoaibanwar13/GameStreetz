
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', LandingPage,name="LandingPage"),
    path('rules/', rules,name="rules"),
    path('playgame/', gamearea,name="playgame"),
    path('submit_score/', submit_score, name='submit_score'),
    path('gameover/', gameover, name='gameover'),
    path('gamewin/', gamewin, name='gamewin'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
