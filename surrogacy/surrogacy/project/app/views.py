from django.shortcuts import render
from django.http import HttpResponse
from app.models import AdminMaster
from app.models import Hospital
from app.models import Registration
from app.models import Appointment
from app.models import Doctors
from app.models import Surrogate
from app.models import Children
from app.models import Receipt



from django.http import JsonResponse
from django.shortcuts import redirect
# from django.core.mail import send_mail
from mailjet_rest import Client
import os





# Create your views here.
def webHome(request):
    return render(request,'web/index.html');

def webAbout(request):
    return render(request,'web/about.html');

def webBlogSingle(request):
    return render(request,'web/blog-single.html');

def webBlog(request):
    return render(request,'web/blog.html');

def webContact(request):
    return render(request,'web/contact.html');

def webHotelSingle(request):
    return render(request,'web/hotel-single.html');

def webHotel(request):
    return render(request,'web/hotel.html');

def webPlaces(request):
    return render(request,'web/places.html');

def webIndex(request):
    return render(request,'web/index.html');

def webAbout(request):
    return render(request,'web/about.html');

def webContact(request):
    return render(request,'web/contact.html');
    
def webRegistration(request):
    return render(request,'web/registration.html');  

def webPrice(request):
    return render(request,'web/price.html');

def webTeam(request):
    return render(request,'web/team.html');

def webTestimonial(request):
    return render(request,'web/testimonial.html');

def webLogin(request):
    return render(request,'web/login.html');

def webHospital(request):
    return render(request,'web/hospital.html');



# admin
def adminHome(request):
    return render(request,'admin/home.html');

def adminTable(request):
    return render(request,'admin/table.html');

def adminAdminmaster(request):
    return render(request,'admin/admin_master.html');

def adminSignin(request):
    return render(request,'admin/signin.html');

def addAdminMaster(request):
    if AdminMaster.objects.filter(ad_email=request.POST['txtEmail'], ad_status='0').exists():
        return HttpResponse("1")
    else:
        lclID = AdminMaster.objects.count()
        status = "0"
    

        lclNewID = lclID + 1

        AdminMaster.objects.create (
            ad_id = lclNewID,
            ad_name = request.POST['txtName'],
            ad_email = request.POST['txtEmail'],
            ad_password = request.POST['txtPassword'],
            ad_mobile = request.POST['txtMobileNo'],    
            ad_status = status,
            # ad_created_by = request.session['email']

        )

        return HttpResponse(request.POST['txtEmail'])

def getAdminData(request):

    products_json = AdminMaster.objects.filter(ad_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def updateAdminData(request):
    AdminMaster.objects.filter(ad_id = request.POST['id']).update(ad_name = request.POST['txtName1'], ad_mobile = request.POST['txtMobileNo1'], ad_email = request.POST['txtEmail1'])
    return HttpResponse()
    # pass

def deleteAdminData(request):

    AdminMaster.objects.filter(ad_id = request.POST['id']).update(ad_status = "1")
    return HttpResponse()


def openHospital(request):
    return render(request,'admin/hospital.html');

def hospitalDetails(request):
    return render(request,'web/hospital_details.html');


def addHospital(request):
    if Hospital.objects.filter(hs_email=request.POST['txtEmail'], hs_status='0').exists():
        return HttpResponse("1")
    else:
        lclID = Hospital.objects.count()
        status = "0"
    

        lclNewID = lclID + 1

        Hospital.objects.create (
            hs_id = lclNewID,
            hs_name = request.POST['txtName'],
            hs_email = request.POST['txtEmail'],
            hs_mobile = request.POST['txtMobileNo'],
            hs_address = request.POST['txtAddress'],    
            hs_image = request.FILES['txtImage'],    
            hs_hrn = request.POST['txtHRN'],    
            hs_hrc = request.FILES['txtHrc'],    
            hs_password = request.POST['txtPassword'],    

            hs_status = status,
            # hr_created_by = request.session['email']

        )

        return HttpResponse(request.POST['txtEmail'])

def getHospitalData(request):

    products_json = Hospital.objects.filter(hs_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def getHospitalSingleData(request):

    products_json = Hospital.objects.filter(hs_id = request.POST['txtID'],hs_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

# login

def loginValidate(request):
    if request.POST['selRole'] == "Admin":
        if AdminMaster.objects.filter(ad_email=request.POST['txtEmail'], ad_password=request.POST['txtPassword'], ad_status='0').exists():
            products_json = AdminMaster.objects.filter(ad_email=request.POST['txtEmail']).values()
            data = list(products_json)
            dictValue = data[0]
            request.session['email'] = dictValue['ad_email']
            request.session['name'] = dictValue['ad_name']

            return HttpResponse(request.POST['selRole'])
        else:
            return HttpResponse("0")

    elif  request.POST['selRole'] == "Hospital":
        if Hospital.objects.filter(hs_email=request.POST['txtEmail'], hs_password=request.POST['txtPassword'], hs_status='0').exists():
            products_json = Hospital.objects.filter(hs_email=request.POST['txtEmail']).values()
            data = list(products_json)
            dictValue = data[0]
            request.session['email'] = dictValue['hs_email']
            request.session['name'] = dictValue['hs_name']

            return HttpResponse(request.POST['selRole'])
        else:
            return HttpResponse("0")

    elif  request.POST['selRole'] == "Doctor":
        if Doctors.objects.filter(dc_email=request.POST['txtEmail'], dc_password=request.POST['txtPassword'], dc_status='0').exists():
            products_json = Doctors.objects.filter(dc_email=request.POST['txtEmail']).values()
            data = list(products_json)
            dictValue = data[0]
            request.session['email'] = dictValue['dc_email']
            request.session['name'] = dictValue['dc_name']
            request.session['hospitalName'] = dictValue['dc_created_by']


            return HttpResponse(request.POST['selRole'])
        else:
            return HttpResponse("0")
    else:
        if Surrogate.objects.filter(sr_email=request.POST['txtEmail'], sr_password=request.POST['txtPassword'], sr_status='0').exists():
                products_json = Surrogate.objects.filter(sr_email=request.POST['txtEmail']).values()
                data = list(products_json)
                dictValue = data[0]
                request.session['email'] = dictValue['sr_email']
                request.session['name'] = dictValue['sr_name']
                request.session['hospitalName'] = dictValue['sr_created_by']


                return HttpResponse(request.POST['selRole'])
        else:
            return HttpResponse("0")


def appointment(request):

    # print(txtName);
    # return render(request, 'admin/admin_master.html');

    if 'web_email' in request.session:
        if Appointment.objects.filter(ap_hospital_name=request.POST['txtName'], ap_user_name=request.session['web_email'], ap_status='0').exists():
            return HttpResponse("1")
        else:
            lclID = Appointment.objects.count()
            status = "0"

            lclNewID = lclID + 1

            Appointment.objects.create (
                ap_id = lclNewID,
                ap_hospital_name = request.POST['txtName'],
                ap_user_name = request.session['web_name'],
                ap_user_email = request.session['web_email'],
                ap_user_phone = request.session['web_phone'],
                ap_status = status,
                # hr_created_by = request.session['email']

            )
            return HttpResponse("success")
    else:
        # print("Hello");
        return HttpResponse("signin")




#hospital
def hospitalHome(request):
    return render(request, 'hospital/home.html');

# user register
def addUser(request):
    if Registration.objects.filter(us_email=request.POST['txtEmail'], us_status='0').exists():
        return HttpResponse("1")
    else:
        lclID = Registration.objects.count()
        status = "0"
    

        lclNewID = lclID + 1

        Registration.objects.create (
            us_id = lclNewID,
            us_name = request.POST['txtName'],
            us_email = request.POST['txtEmail'],
            us_password = request.POST['txtPassword'],
            us_mobile = request.POST['txtMobileNo'],    
            us_status = status,
            # ad_created_by = request.session['email']

        )

        return HttpResponse(request.POST['txtEmail'])

def webLogin(request):
    return render(request,'web/login.html');

def userLoginValidate(request):
    if Registration.objects.filter(us_email=request.POST['txtEmail'], us_password=request.POST['txtPassword'], us_status='0').exists():
        products_json = Registration.objects.filter(us_email=request.POST['txtEmail']).values()
        data = list(products_json)
        dictValue = data[0]
        request.session['web_email'] = dictValue['us_email']
        request.session['web_name'] = dictValue['us_name']
        request.session['web_phone'] = dictValue['us_mobile']
        return HttpResponse("1")
    else:
        return HttpResponse("0")

def getAppointmentRequests(request):
    products_json = Appointment.objects.filter(ap_hospital_name = request.session['name'],ap_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value


def openAppointmentRequests(request):
    return render(request,'hospital/appointment_request.html');

def setAppointment(request):
    Appointment.objects.filter(ap_id = request.POST['id']).update(ap_request_status = 'Request Accepted')

    products_json = Appointment.objects.filter(ap_id = request.POST['id']).values()
    data = list(products_json)
    dictValue = data[0]
   

    print(dictValue['ap_user_email']);
    api_key = 'aac6730a0dc8a5b7c81cf4c35f650567'
    api_secret = '5f1c7d8729dd7e93b78796ad6ba7697f'
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
      'Messages': [
        {
          "From": {
            "Email": "shaheenkadakol@gmail.com",
            "Name": "shaheen"
          },
          "To": [
            {
              "Email": dictValue['ap_user_email'],
              "Name": "shaheen"
            }
          ],
          "Subject": "Greetings from Surrogacy.",
          "TextPart": "Surrogacy",
          "HTMLPart": "<h3>Dear Patient, welcome</h3><br /> You Appointment has scheduled on " + request.POST['date'],
          "CustomID": "AppGettingStartedTest"
        }
      ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())

    return HttpResponse()

# doctors
def openDoctor(request):
    return render(request,'hospital/doctors.html');


def doctorDetails(request):
    if request.POST['action'] == "add":
        if Doctors.objects.filter(dc_email=request.POST['txtEmail'], dc_status='0').exists():
            return HttpResponse("1")
        else:
            lclID = Doctors.objects.count()
            status = "0"
        

            lclNewID = lclID + 1
            Doctors.objects.create (
                dc_id = lclNewID,
                dc_name = request.POST['txtName'],
                dc_email = request.POST['txtEmail'],
                dc_password = request.POST['txtPassword'],
                dc_mobile = request.POST['txtMobileNo'],    
                dc_status = status,
                dc_created_by = request.session['email']
                )
            return HttpResponse()

    elif request.POST['action'] == "getData":
       products_json = Doctors.objects.filter(dc_status='0').values()
       data = list(products_json)
       value = JsonResponse(data, safe=False)
       return value

    elif request.POST['action'] == "update":
        data = Doctors.objects.filter(dc_id=request.POST['id']).update(
            dc_name = request.POST['txtName1'], 
            dc_mobile = request.POST['txtMobileNo1'], 
            dc_email = request.POST['txtEmail1']
        );

    elif request.POST['action'] == "delete":
        data = Doctors.objects.filter(dc_id=request.POST['id']).update(
            dc_status='1'
        );


    return HttpResponse()

# surrogates
def openSurrogates(request):
    return render(request,'hospital/surrogates.html');


def surrogateDetails(request):
    if request.POST['action'] == "add":
        if Surrogate.objects.filter(sr_email=request.POST['txtEmail'], sr_status='0').exists():
            return HttpResponse("1")
        else:
            lclID = Doctors.objects.count()
            status = "0"
            lclNewID = lclID + 1
            Surrogate.objects.create (
                sr_id = lclNewID,
                sr_doctor = request.POST['selDoctor'],
                sr_name = request.POST['txtName'],
                sr_email = request.POST['txtEmail'],
                sr_password = request.POST['txtPassword'],
                sr_mobile = request.POST['txtMobileNo'], 
                sr_aadhar = request.FILES['txtAadhar'],    
                sr_status = status,
                sr_created_by = request.session['email'],
                )
            return HttpResponse()

    elif request.POST['action'] == "getData":
       products_json = Surrogate.objects.filter(sr_status='0').values()
       data = list(products_json)
       value = JsonResponse(data, safe=False)
       return value

    elif request.POST['action'] == "update":
        data = Surrogate.objects.filter(sr_id=request.POST['id']).update(
            sr_doctor = request.POST['selDoctor1'],     
            sr_name = request.POST['txtName1'], 
            sr_mobile = request.POST['txtMobileNo1'], 
            sr_email = request.POST['txtEmail1']
        );

    elif request.POST['action'] == "delete":
        data = Surrogate.objects.filter(sr_id=request.POST['id']).update(
            sr_status='1'
        );


    return HttpResponse()

# parent info
def parentInfo(request):
    return render(request,'hospital/parent_info.html');

def getParentInfo(request):
    products_json = Appointment.objects.filter(ap_request_status = "Request Accepted", ap_hospital_name = request.session['name'],ap_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def getDoctorInfo(request):
    products_json = Doctors.objects.filter(dc_created_by = request.session['email'],dc_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def assignDoctor(request):
    Appointment.objects.filter(ap_id = request.POST['id']).update(ap_doctor = request.POST['selDoctor'])
    return HttpResponse()

def doctorIndex(request):
    return render(request, 'doctor/home.html');

def openDoctorParentDetails(request):
    return render(request, 'doctor/doctor_parent_details.html');

def singleParentDetails(request):
    products_json = Appointment.objects.filter(ap_doctor = request.session['name'],ap_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def getHospitalSurrogates(request):
    products_json = Surrogate.objects.filter(sr_created_by = request.session['hospitalName'],sr_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def assignSurrogates(request):
    Appointment.objects.filter(ap_id = request.POST['id']).update(ap_surrogates = request.POST['selSurrogates'])
    return HttpResponse()

def surrogateIndex(request):
    return render(request, 'surrogate/surrogate_index.html');

def openManageChildrens(request):
    return render(request, 'surrogate/manage_children.html');

def getSurrogateParent(request):
    products_json = Appointment.objects.filter(ap_surrogates = request.session['name'],ap_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def childrenDetails(request):
    if request.POST['action'] == "add":
        if Children.objects.filter(ch_status='0').exists():
            return HttpResponse("1")
        else:
            lclID = Children.objects.count()
            status = "0"
        

            lclNewID = lclID + 1
            Children.objects.create (
                ch_id = lclNewID,
                ch_name = request.POST['txtName'],
                ch_hospital_name = request.session['hospitalName'],
                ch_parent_name = request.POST['selParent'],
                ch_status = status,
                ch_created_by = request.session['email']
                )
            return HttpResponse()

    elif request.POST['action'] == "getData":
       products_json = Children.objects.filter(ch_status='0').values()
       data = list(products_json)
       value = JsonResponse(data, safe=False)
       return value

    elif request.POST['action'] == "update":
        data = Children.objects.filter(ch_id=request.POST['id']).update(
            ch_name = request.POST['txtName1'], 
            ch_parent_name = request.POST['selParent1'], 
        );

    elif request.POST['action'] == "delete":
        data = Children.objects.filter(ch_id=request.POST['id']).update(
            ch_status='1'
        );


    return HttpResponse()

def openSurrogateParentDetails(request):
    return render(request, 'surrogate/surrogate_parent_details.html');

def surrogateParentDetails(request):
    products_json = Appointment.objects.filter(ap_surrogates = request.session['name'],ap_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def openChildrenInfo(request):
    return render(request, 'hospital/children_info.html');

def childInfoDetails(request):
    products_json = Children.objects.filter(ch_hospital_name = request.session['email'],ch_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value


def openGenerateReceipt(request):
    return render(request, 'hospital/generate_receipt.html');

def getChildInfo(request):
    products_json = Children.objects.filter(ch_parent_name = request.POST['selParent'],ch_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def generateReceipt(request):
    if Receipt.objects.filter(re_parent_name = request.POST['selParent'],re_status='0').exists():
        return HttpResponse("1")
    else:
        lclID = Receipt.objects.count()
        status = "0"
        lclNewID = lclID + 1

        Receipt.objects.create (
            re_id = lclNewID,
            re_child_count = request.POST['no_of_children'],
            re_hospital_name = request.session['name'],
            re_parent_name = request.POST['selParent'], 
            re_amount = request.POST['amount'], 
            re_status = status,
            re_created_by = request.session['email']

        )

        return HttpResponse()

def checkUserSession(request):
    if "web_email" in request.session:
        return HttpResponse(1)
    else:
        return HttpResponse(0)

def webLogout(request):
    request.session.delete()
    return render(request,'web/index.html')

def openWebProfile(request):
    data = Registration.objects.filter(us_email = request.session['web_email']).values()
    data1 = Receipt.objects.filter(re_parent_name = request.session['web_name']).values()
    context = {};
    context1 = {}
    context['user'] = list(data);
    context1['receipt'] = list(data1);

    print(context)
    return render(request, 'web/profile.html', {"a":list(data), "b":list(data1)});

def surrogacyPayment(request):
    Receipt.objects.filter(re_id = request.POST['txtID']).update(re_payment_status = "success")
    return HttpResponse()

def paySuccess(request):
    return render(request,'web/pay_success.html')

def paymentDetails(request):
    products_json = Receipt.objects.filter(re_payment_status = "success",re_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def openPaymentDetails(request):
    return render(request,'admin/payment_details.html')

def openHospitalPaymentDetails(request):
    return render(request,'hospital/payment_details.html')

def paymentDetailsHospital(request):
    products_json = Receipt.objects.filter(re_hospital_name = request.session['name'],re_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def openSurrogatePaymentDetails(request):
    return render(request,'surrogate/payment_details.html')

def paymentDetailSurrogate(request):
    # print(request.session['hospitalName'])
    products_json = Receipt.objects.filter(re_created_by = request.session['hospitalName'],re_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value

def updateHospitalData(request):
    Hospital.objects.filter(hs_id = request.POST['id']).update(hs_name = request.POST['txtName1'], hs_mobile = request.POST['txtMobileNo1'], hs_address = request.POST['txtAddress1'], hs_hrn = request.POST['txtHRN1'],hs_email = request.POST['txtEmail1'])
    return HttpResponse()

def deleteHospitalData(request):

    Hospital.objects.filter(hs_id = request.POST['id']).update(hs_status = "1")
    return HttpResponse()


def childrenInfoDoctor(request):
    return render(request,'doctor/children_info.html')


def childInfoDetailsDoctor(request):
    products_json = Children.objects.filter(ch_hospital_name =  request.session['hospitalName'],ch_status='0').values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value



