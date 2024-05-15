from django.shortcuts import render ,redirect ,get_object_or_404
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import uuid
from django.db import transaction

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

from .forms import UserForm
from .forms import DoctorForm
from .forms import DoctorAppointmentForm
from .forms import DoctorSpecializationForm
from .forms import MedicineForm
from .forms import MessageForm
from .forms import NurseForm
from .forms import NurseAppointmentForm
from .forms import SanatoriumForm
from .forms import SanatoriumAppointmentForm

from .forms import LoginForm
# Create your views here.


# def aboutus(request):
#     return render(request,'aboutUs.html')

# def books(request):
#     return render(request,'books.html')

# def contactus(request):
#     return render(request,'contactUs.html')

# def doctorbooking(request):
#     return render(request,'doctorBooking.html')

# def nursebooking(request):
#     return render(request,'nurseBooking.html')

# def sanatoriumbooking(request):
#     return render(request,'sanatoriumBooking.html')

# def profile(request):
#     return render(request,'profile.html')

# def treatment(request):
#     return render(request,'treatment.html')

# def videos(request):
#     return render(request,'videos.html')
def aboutus(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'aboutUs.html', {'user': user})

def books(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'books.html', {'user': user})

def contactus(request,user_id):
    user = User.objects.get(user_id=user_id)
    
    if request.method == 'POST':
        message_box = request.POST.get('message-box', '')
        messageid=int(uuid.uuid4().hex[:8], 16)
        messageid%=100000
        message = Message.objects.create(user=user,message_id=messageid, message_description=message_box)
    return render(request, 'contactUs.html', {'user': user})


    
def doctorbooking(request,user_id):
    user = User.objects.get(user_id=user_id)
    
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor_name')
        fname,lname=doctor_name.split()
        doctor=Doctor.objects.get(doctor_fname=fname.lower())
        appointmentDate=request.POST['date']
        appointmentTime=request.POST['time']
        illnessDescription=request.POST['description']
        address=request.POST['address']
        appointment=DoctorAppointment(user=user,doctor=doctor,appointment_date=appointmentDate,appointment_address=address,appointment_time=appointmentTime,illness_description=illnessDescription)
        appointment.save()
    return render(request, 'doctorBooking.html', {'user': user})


def nursebooking(request,user_id):
    user = User.objects.get(user_id=user_id)
    
    if request.method == 'POST':
        nurse_name = request.POST.get('nurse_name')
        fname,lname=nurse_name.split()
        nurse=Nurse.objects.get(nurse_fname=fname.lower())
        appointmentDate=request.POST['date']
        appointmentTime=request.POST['time']
        illnessDescription=request.POST['description']
        address=request.POST['address']
        appointment=NurseAppointment(user=user,nurse=nurse,appointment_date=appointmentDate,appointment_address=address,appointment_time=appointmentTime,illness_description=illnessDescription)
        appointment.save()
    return render(request, 'nurseBooking.html', {'user': user})


def sanatoriumbooking(request,user_id):
    user = User.objects.get(user_id=user_id)
    
    if request.method == 'POST':
        sanatorium_name = request.POST.get('sanatorium_name')
        sanatorium=Sanatorium.objects.get(sanatorium_name=sanatorium_name.lower())
        appointmentDate=request.POST['date']
        appointmentTime=request.POST['time']
        illnessDescription=request.POST['message']
        address=request.POST['address']
        appointment=SanatoriumAppointment(user=user,sanatorium=sanatorium,appointment_address=address,appointment_date=appointmentDate,appointment_time=appointmentTime,illness_description=illnessDescription)
        appointment.save()

    return render(request, 'sanatoriumBooking.html', {'user': user})

def profile(request,user_id):
    user = User.objects.get(user_id=user_id)
    doctorappointments=DoctorAppointment.objects.filter(user=user).select_related('doctor')
    nurseappointments=NurseAppointment.objects.filter(user=user).select_related('nurse')
    sanatoriumappointments=SanatoriumAppointment.objects.filter(user=user).select_related('sanatorium')
    messages=Message.objects.filter(user=user)
    return render(request, 'profile.html', {'user': user, 'doctorappointments':doctorappointments,'messages':messages, 'nurseappointments':nurseappointments, 'sanatoriumappointments':sanatoriumappointments})

def treatment(request,user_id):
    user = User.objects.get(user_id=user_id)
    if request.method=='POST':
        medicineName=request.POST.get('medicine-name')
        medicineDescription=request.POST.get('medicine-description')
        medicineid=int(uuid.uuid4().hex[:8], 16) %100000
        if medicineName and medicineDescription:
            medicine = Medicine(user=user,medicine_id=medicineid, medicine_name=medicineName, medicine_description=medicineDescription)
            medicine.save()
        return redirect('treatment', user_id=user.user_id)
    treatments=Medicine.objects.filter(user=user)
    return render(request, 'treatment.html', {'user': user,'treatments':treatments})

def deleteTreatment(request,medicine_id,user_id):
    medicine=get_object_or_404(Medicine,pk=medicine_id)
    if request.method=='POST':
        medicine.delete()
        return redirect('treatment', user_id=user_id)
    else:
        pass

def takenTreatment(request,medicine_id,user_id):
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    if request.method == 'POST':
        medicine.medicine_istaken = 'taken'
        medicine.save()
    return redirect('treatment', user_id=user_id)

def untakenTreatment(request,medicine_id,user_id):
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    if request.method == 'POST':
        medicine.medicine_istaken = 'untaken'
        medicine.save()
    return redirect('treatment', user_id=user_id)

def videos(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'videos.html', {'user': user})


def authenticate_user(username, password):
    try:
        user = User.objects.get(user_username=username, user_password=password)
        return user  
    except User.DoesNotExist:
        return None  

def login(request):
    if request.method == 'POST':
        username = request.POST.get('login-username')
        password = request.POST.get('login-pass')
        if not username or not password:
            messages.error(request,'Please complete all fields')      
            return render(request, 'loginSignup.html', {})

        user = authenticate_user(username, password)
        if user is not None:
            return render(request, 'index.html', {'user': user})
        else:
            messages.error(request,'username or password are not correct')
            return render(request, 'loginSignup.html', {})                                  
    else:
        return render(request, 'loginSignup.html', {})

@login_required
def index(request):
    # user = User.objects.get(user_id=user_id)
    return render(request,'index.html',{{user}})

def index2(request,user_id):                                          #the home return from another page 
    user = User.objects.get(user_id=user_id)
    return render(request, 'index.html', {'user': user})

def signup(request):
    fname=request.POST['firstname']
    lname=request.POST['lastname']
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    cnfrmpassword=request.POST['cnfrmpassword']
    gender=request.POST['gender'].lower()
    location=request.POST['location'].lower()
    date=request.POST['date']
    phone=request.POST['phone']
    city, street=location.split()

    user=User(user_fname=fname,user_lname=lname,user_gmail=email,user_username=username,user_password=password,user_gender=gender,user_street=street,user_city=city,user_phone=phone,user_birthdate=date)
    user.save()
    return redirect('login')



# -------------------------------------------
# blogs views
def blog1(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'blog1.html', {'user': user})

def blog2(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'blog2.html', {'user': user})

def blog3(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'blog3.html', {'user': user})

def blog4(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'blog4.html', {'user': user})

def blog5(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'blog5.html', {'user': user})

def blog6(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'blog6.html', {'user': user})

def blog7(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'blog7.html', {'user': user})

def blog8(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'blog8.html', {'user': user})

def blog9(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'blog9.html', {'user': user})

def blog10(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'blog10.html', {'user': user})


# -------------------------------------------
# doctors views
def doctor1(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'doctor1.html', {'user': user})

def doctor2(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'doctor2.html', {'user': user})

def doctor3(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'doctor3.html', {'user': user})

def doctor4(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'doctor4.html', {'user': user})

def doctor5(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'doctor5.html', {'user': user})

def doctor6(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'doctor6.html', {'user': user})

def doctor7(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'doctor7.html', {'user': user})

def doctor8(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'doctor8.html', {'user': user})

#--------------------------------------------
#nurses views

def nurse1(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'nurse1.html', {'user': user})

def nurse2(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'nurse2.html', {'user': user})

def nurse3(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'nurse3.html', {'user': user})

def nurse4(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'nurse4.html', {'user': user})

def nurse5(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'nurse5.html', {'user': user})

def nurse6(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'nurse6.html', {'user': user})

def nurse7(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'nurse7.html', {'user': user})

def nurse8(request,user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'nurse8.html', {'user': user})


