from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views import View
from .models import Patient
from .forms import PatientForm


class HomePageView(TemplateView):
    template_name = "mainapp/index.html"


class LogInRegistration(TemplateView):
    template_name = "mainapp/login_reg.html"


class Registration(TemplateView):
    template_name = "mainapp/registration.html"


class PatientListView(View):
    def get(self, request):
        patients = Patient.objects.all()
        return render(request, 'mainapp/patient_list.html', {'patients': patients})


class AddPatientView(View):
    def get(self, request):
        form = PatientForm()
        return render(request, 'mainapp/add_patient.html', {'form': form})

    def post(self, request):
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
        return render(request, 'mainapp/add_patient.html', {'form': form})


class EditPatientView(View):
    def get(self, request, pk):
        patient = Patient.objects.get(pk=pk)
        form = PatientForm(instance=patient)
        return render(request, 'mainapp/edit_patient.html', {'form': form})

    def post(self, request, pk):
        patient = Patient.objects.get(pk=pk)
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
        return render(request, 'mainapp/edit_patient.html', {'form': form})


class DeletePatientView(View):
    def get(self, request, pk):
        patient = Patient.objects.get(pk=pk)
        return render(request, 'delete_patient.html', {'patient': patient})

    def post(self, request, pk):
        patient = Patient.objects.get(pk=pk)
        patient.delete()
        return redirect('patient_list')
