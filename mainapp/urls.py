from django.urls import path
from .views import HomePageView,LogInRegistration,Registration
urlpatterns = [
 path("", HomePageView.as_view(), name="home"),
 path("login", LogInRegistration.as_view(), name="login"),
path("register", Registration.as_view(), name="register"),
]
