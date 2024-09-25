"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.webHome),
    path('index/',views.webHome),
    path('surrogacyIndex/',views.webHome),

    path('',views.webHome),
    path('login/',views.webLogin),
    path('about/',views.webAbout),
    path('blog-single/',views.webBlogSingle),
    path('blog/',views.webBlog),
    path('contact/',views.webContact),
    path('hotel-single/',views.webHotelSingle),
    path('hotel/',views.webHotel),
    path('places/',views.webPlaces),
    path('index/',views.webIndex),
    path('webcontact/',views.webContact),
    path('about/',views.webAbout),
    path('registration/',views.webRegistration),
    path('price/',views.webPrice),
    path('team/',views.webTeam),
    path('testimonial/',views.webTestimonial),
    path('webHospital/',views.webHospital),

    # admin
     # path('home/',views.adminHome),
    path('table/',views.adminTable),
    path('admin_index/',views.adminHome),

    path('admin_master/',views.adminAdminmaster),

    path('signin/',views.adminSignin),


    # hospital
    path('hospital_index/',views.hospitalHome),

    
    # admin
    path('add/admin_master/', views.addAdminMaster),
    path('get_data/admin_master/', views.getAdminData, name='admin_master'),
    path('update/admin_master/', views.updateAdminData, name='admin_master'),
    path('delete/admin_master/', views.deleteAdminData, name='admin_master'),

    # hospital
    path('hospital/',views.openHospital),
    path('add/hospital/', views.addHospital),
    path('get_data/hospital/', views.getHospitalData, name='admin_master'),

    path('hospital_details/', views.hospitalDetails, name='hospital_details'),
    path('get_data/hospital_single/', views.getHospitalSingleData, name='admin_master'),

    # login
    path('login_validate/', views.loginValidate),

    path('appointment/', views.appointment),
    # path('take_appointment/', views.takeAppointment),
    path('login/', views.webLogin),
    path('user_login_validate/', views.userLoginValidate),


     
    path('add/user/', views.addUser),
    path('appointment_request_page/', views.openAppointmentRequests, name='appointment_requests'),

    path('appointment_requests/', views.getAppointmentRequests, name='appointment_requests'),
    path('setAppointment/', views.setAppointment, name='appointment_requests'),


    # doctors
    path('doctors/', views.openDoctor),
    path('doctor_details/', views.doctorDetails),

    # surrogates
    path('surrogates/', views.openSurrogates),
    path('surrogate_details/', views.surrogateDetails),

    # parent info
    path('parent_info/', views.parentInfo),
    path('get_data/parent_info/', views.getParentInfo),

    path('get_data/doctor/', views.getDoctorInfo),
    path('assignDoctor/', views.assignDoctor),

    # doctor
    path('doctor_index/', views.doctorIndex),
    path('doctor_parent_details/', views.openDoctorParentDetails),

    path('single_parent_details/', views.singleParentDetails),

    path('get_data/hospital_surrogates/', views.getHospitalSurrogates),
    path('assign_surrogates/', views.assignSurrogates),

    path('surrogate_index/', views.surrogateIndex),
    path('open_manage_childrens/', views.openManageChildrens),

    path('get_data/surrogate_parent/', views.getSurrogateParent),

    path('children_details/', views.childrenDetails),

    path('open_surrogate_parent_details/', views.openSurrogateParentDetails),

    path('surrogate_parent_details/', views.surrogateParentDetails),

    path('children_info/', views.openChildrenInfo),

    path('child_info_details/', views.childInfoDetails),

    path('open_generate_receipt/', views.openGenerateReceipt),
    path('get_child_info/', views.getChildInfo),

    path('generate_receipt/', views.generateReceipt),
    path('check_user_session/', views.checkUserSession),

    path('webLogout/', views.webLogout),

    path('webProfile/', views.openWebProfile),
    path('surrogacy_payment/', views.surrogacyPayment),

    path('pay_success/', views.paySuccess),
    path('open_payment_details/', views.openPaymentDetails),

    path('payment_details/', views.paymentDetails),

    path('open_hospital_payment_details/', views.openHospitalPaymentDetails),
    path('payment_details_hospital/', views.paymentDetailsHospital),

    path('open_surrogate_payment_details/', views.openSurrogatePaymentDetails),
    path('payment_details_surrogate/', views.paymentDetailSurrogate),

    path('update/hospital/', views.updateHospitalData, name='hospital'),
    path('delete/hospital/', views.deleteHospitalData, name='hospital'), 


    path('children_info_doctor/', views.childrenInfoDoctor),

    path('child_info_details_doctor/', views.childInfoDetailsDoctor),








]
