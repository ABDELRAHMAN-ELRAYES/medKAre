from django.forms import ModelForm
from django import forms

from .models import User
from .models import Doctor
from .models import DoctorAppointment
from .models import DoctorSpecialization
from .models import Medicine
from .models import Message
from .models import Nurse
from .models import NurseAppointment
from .models import Sanatorium
from .models import SanatoriumAppointment


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class UserForm(ModelForm):
    class Meta:
        model:User
        fields:'__all__'

class DoctorForm(ModelForm):
    class Meta:
        model:Doctor
        fields:'__all__'

class DoctorAppointmentForm(ModelForm):
    class Meta:
        model:DoctorAppointment
        fields:'__all__'

class DoctorSpecializationForm(ModelForm):
    class Meta:
        model:DoctorSpecialization
        fields:'__all__'

class NurseForm(ModelForm):
    class Meta:
        model:Nurse
        fields:'__all__'

class NurseAppointmentForm(ModelForm):
    class Meta:
        model:NurseAppointment
        fields:'__all__'

class SanatoriumForm(ModelForm):
    class Meta:
        model:Sanatorium
        fields:'__all__'

class MedicineForm(ModelForm):
    class Meta:
        model:Medicine
        fields:'__all__'

class MessageForm(ModelForm):
    class Meta:
        model:Message
        fields:'__all__'

class SanatoriumAppointmentForm(ModelForm):
    class Meta:
        model:SanatoriumAppointment
        fields:'__all__'
