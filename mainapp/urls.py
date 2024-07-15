from django.urls import path
from .views import HomePageView,LogInRegistration
urlpatterns = [
 path("", HomePageView.as_view(), name="home"),
 path("login", LogInRegistration.as_view(), name="login"),
]
