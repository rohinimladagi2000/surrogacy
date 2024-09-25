from django.db import models
from datetime import datetime    


# Create your models here.

class AdminMaster(models.Model):
	ad_id = models.AutoField(primary_key=True, unique = True)
	ad_name = models.CharField(max_length=100)
	ad_mobile = models.CharField(max_length=100)
	ad_email = models.CharField(max_length=100)
	ad_password = models.CharField(max_length=100)
	ad_status = models.CharField(max_length=100,default="0")
	ad_created_by = models.CharField(max_length=100)

class Hospital(models.Model):
	hs_id = models.AutoField(primary_key=True, unique = True)
	hs_name = models.CharField(max_length=100)
	hs_email = models.CharField(max_length=100)
	hs_mobile = models.CharField(max_length=100)
	hs_address = models.CharField(max_length=100)
	hs_image = models.FileField(upload_to="app/static/media/image")
	hs_hrn = models.CharField(max_length=100)
	hs_hrc =  models.FileField(upload_to="app/static/media/hrc")
	hs_password = models.CharField(max_length=100)
	hs_status = models.CharField(max_length=100,default="0")
	hs_created_by = models.CharField(max_length=100)

class Appointment(models.Model):
	ap_id = models.AutoField(primary_key=True, unique = True)
	ap_hospital_name = models.CharField(max_length=100)
	ap_user_name = models.CharField(max_length=100)
	ap_user_email = models.CharField(max_length=100,default = '')
	ap_user_phone = models.CharField(max_length=100,default = '')
	ap_request_status = models.CharField(max_length=100)
	ap_doctor = models.CharField(max_length=100,default = '')
	ap_surrogates = models.CharField(max_length=100,default = '')
	ap_status = models.CharField(max_length=100,default="0")
	ap_created_by = models.CharField(max_length=100)

class Registration(models.Model):
	us_id = models.AutoField(primary_key=True, unique = True)
	us_name = models.CharField(max_length=100)
	us_mobile = models.CharField(max_length=100)
	us_email = models.CharField(max_length=100)
	us_password = models.CharField(max_length=100)
	us_status = models.CharField(max_length=100,default="0")
	us_created_by = models.CharField(max_length=100)

class Doctors(models.Model):
	dc_id = models.AutoField(primary_key=True, unique = True)
	dc_name = models.CharField(max_length=100)
	dc_mobile = models.CharField(max_length=100)
	dc_email = models.CharField(max_length=100)
	dc_password = models.CharField(max_length=100)
	dc_status = models.CharField(max_length=100,default="0")
	dc_created_by = models.CharField(max_length=100)

class Surrogate(models.Model):
	sr_id = models.AutoField(primary_key=True, unique = True)
	sr_name = models.CharField(max_length=100)
	sr_mobile = models.CharField(max_length=100)
	sr_email = models.CharField(max_length=100)
	sr_password = models.CharField(max_length=100)
	sr_aadhar = models.FileField(upload_to="app/static/media/aadhar")
	sr_doctor = models.CharField(max_length=100,default = '')
	sr_status = models.CharField(max_length=100,default="0")
	sr_created_by = models.CharField(max_length=100)

class Children(models.Model):
	ch_id = models.AutoField(primary_key=True, unique = True)
	ch_name = models.CharField(max_length=100)
	ch_hospital_name = models.CharField(max_length=100)
	ch_parent_name = models.CharField(max_length=100)
	ch_status = models.CharField(max_length=100,default="0")
	ch_created_by = models.CharField(max_length=100)

class Receipt(models.Model):
	re_id = models.AutoField(primary_key=True, unique = True)
	re_child_count = models.CharField(max_length=100)
	re_hospital_name = models.CharField(max_length=100)
	re_parent_name = models.CharField(max_length=100)
	re_amount = models.CharField(max_length=100,default = '')
	re_payment_status = models.CharField(max_length=100,default = '')	
	re_status = models.CharField(max_length=100,default="0")	
	re_created_by = models.CharField(max_length=100)
	re_created_date =  models.DateTimeField(default=datetime.now, blank=True)




