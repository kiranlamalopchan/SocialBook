
from django.urls import path
from webapp.views import IndexView
from webapp.views import ProfileView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("profile/", ProfileView.as_view(), name="profile")
]
