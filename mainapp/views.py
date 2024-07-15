from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "mainapp/index.html"


class LogInRegistration(TemplateView):
    template_name = "mainapp/login_reg.html"
