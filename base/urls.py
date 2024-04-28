from django.urls import path
from . import views


urlpatterns=[
    path('',views.login,name='login'),
    path('home/',views.index,name='index'),
    path('home/<int:user_id>/',views.index2,name='index2'),
    path('aboutus/<int:user_id>/',views.aboutus,name='aboutus'),
    path('books/<int:user_id>/',views.books,name='books'),
    path('contactus/<int:user_id>/',views.contactus,name='contactus'),
    path('doctorbooking/<int:user_id>/',views.doctorbooking,name='doctorbooking'),
    path('nursebooking/<int:user_id>/',views.nursebooking,name='nursebooking'),
    path('profile/<int:user_id>/appointments/messages/',views.profile,name='profile'),
    path('sanatoriumbooking/<int:user_id>/',views.sanatoriumbooking,name='sanatoriumbooking'),
    path('treatment/<int:user_id>/',views.treatment,name='treatment'),
    path('videos/<int:user_id>/',views.videos,name='videos'),
    path('signup/',views.signup,name='signup'),

    path('blog1/<int:user_id>/',views.blog1,name='blog1'),
    path('blog2/<int:user_id>/',views.blog2,name='blog2'),
    path('blog3/<int:user_id>/',views.blog3,name='blog3'),
    path('blog4/<int:user_id>/',views.blog4,name='blog4'),
    path('blog5/<int:user_id>/',views.blog5,name='blog5'),
    path('blog6/<int:user_id>/',views.blog6,name='blog6'),
    path('blog7/<int:user_id>/',views.blog7,name='blog7'),
    path('blog8/<int:user_id>/',views.blog8,name='blog8'),
    path('blog9/<int:user_id>/',views.blog9,name='blog9'),
    path('blog10/<int:user_id>/',views.blog10,name='blog10'),



    path('doctor1/<int:user_id>/',views.doctor1,name='doctor1'),
    path('doctor2/<int:user_id>/',views.doctor2,name='doctor2'),
    path('doctor3/<int:user_id>/',views.doctor3,name='doctor3'),
    path('doctor4/<int:user_id>/',views.doctor4,name='doctor4'),
    path('doctor5/<int:user_id>/',views.doctor5,name='doctor5'),
    path('doctor6/<int:user_id>/',views.doctor6,name='doctor6'),
    path('doctor7/<int:user_id>/',views.doctor7,name='doctor7'),
    path('doctor8/<int:user_id>/',views.doctor8,name='doctor8'),

    path('nurse1/<int:user_id>/',views.nurse1,name='nurse1'),
    path('nurse2/<int:user_id>/',views.nurse2,name='nurse2'),
    path('nurse3/<int:user_id>/',views.nurse3,name='nurse3'),
    path('nurse4/<int:user_id>/',views.nurse4,name='nurse4'),
    path('nurse5/<int:user_id>/',views.nurse5,name='nurse5'),
    path('nurse6/<int:user_id>/',views.nurse6,name='nurse6'),
    path('nurse7/<int:user_id>/',views.nurse7,name='nurse7'),
    path('nurse8/<int:user_id>/',views.nurse8,name='nurse8'),
]