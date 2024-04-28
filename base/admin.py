from django.contrib import admin

# Register your models here.
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

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(DoctorAppointment)
admin.site.register(DoctorSpecialization)
admin.site.register(Medicine)
admin.site.register(Message)
admin.site.register(Nurse)
admin.site.register(NurseAppointment)
admin.site.register(Sanatorium)
admin.site.register(SanatoriumAppointment)

