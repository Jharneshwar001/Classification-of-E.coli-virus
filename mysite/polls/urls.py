from django.urls import path

from mysite.polls.views import handler


urlpatterns = [
    path('home/', handler, name='homepage'),
    ]