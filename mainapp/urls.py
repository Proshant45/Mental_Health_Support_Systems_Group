from django.urls import path
from .views import HomePageView, LogInRegistration, Registration, PatientListView, AddPatientView, EditPatientView, DeletePatientView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("login", LogInRegistration.as_view(), name="login"),
    path("register", Registration.as_view(), name="register"),
    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patients/add/', AddPatientView.as_view(), name='add_patient'),
    path('patients/edit/<int:pk>/', EditPatientView.as_view(), name='edit_patient'),
    path('patients/delete/<int:pk>/',
         DeletePatientView.as_view(), name='delete_patient'),
]
