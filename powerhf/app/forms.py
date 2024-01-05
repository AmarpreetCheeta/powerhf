from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.core.exceptions import ValidationError
from app.models import *

DEPARTMENTS = (
    ('Choose department','Choose department'),
    ('HR','HR'),
    ('IT','IT'),
    ('Accounts','Accounts'),
    ('CAD','CAD'),
    ('SCM','SCM'),
    ('Technical','Technical'),
)

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(
        attrs={'class': 'input-form input-sign-form', 'placeholder': 'Enter your username', 'id':'autoSizingInputGroup'}
    ))
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(
        attrs={'class': 'input-form input-sign-form', 'placeholder': 'Enter your first name', 'id':'autoSizingInputGroup'}
    ))
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput(
        attrs={'class': 'input-form input-sign-form', 'placeholder': 'Enter your last name', 'id':'autoSizingInputGroup'}
    ))
    email = forms.CharField(label='Email Address',widget=forms.EmailInput(
        attrs={'class': 'input-form input-sign-form', 'placeholder': 'Enter your email address', 'id':'autoSizingInputGroup'}
    ))
    department = forms.ChoiceField(choices=DEPARTMENTS,label='Department',widget=forms.Select(
        attrs={'class': 'input-form input-sign-form'}
    ))
    password1 = forms.CharField(label='Department',widget=forms.PasswordInput(
        attrs={'class': 'input-form input-sign-form', 'placeholder': 'Enter your password', 'id':'autoSizingInputGroup'}
    ))
    password2 = forms.CharField(label='Department',widget=forms.PasswordInput(
        attrs={'class': 'input-form input-sign-form', 'placeholder': 'Enter your confirm password', 'id':'autoSizingInputGroup'}
    ))

    class Meta:
        model = Users
        fields = ['username','first_name','last_name','email','department']

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if Users.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        return username
        
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if Users.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.pop('autofocus',None)


class UserAuthentication(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'input-form', 'placeholder': 'Enter your email address', 'id':'autoSizingInputGroup'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input-form', 'placeholder': 'Enter your password', 'id':'autoSizingInputGroup'}
    ))




class DieselFillingOrReadingForm(forms.ModelForm):
    DG_HMR_Reading = forms.CharField(required=False, widget=forms.NumberInput(
        attrs={'class':'inputformsfill'}
    ))
    Current_DG_PIU_Reading = forms.CharField(required=False, widget=forms.NumberInput(
        attrs={'class':'inputformsfill'}
    ))
    Total_DC_Load = forms.CharField(required=False, widget=forms.NumberInput(
        attrs={'class':'inputformsfill'}
    ))
    Total_EB_KWH_Reading_from_all_Channels = forms.CharField(required=False, widget=forms.NumberInput(
        attrs={'class':'inputformsfill'}
    ))
    Diesel_Balance_Before_Filling = forms.CharField(required=False, widget=forms.NumberInput(
        attrs={'class':'inputformsfill amount', 'id':'DieselBefroe'}
    ))
    Fuel_Qty_Filled = forms.CharField(required=False, widget=forms.NumberInput(
        attrs={'class':'inputformsfill amount', 'id':'FuelQFilled'}
    ))
    Current_Diesel_Balance = forms.CharField(disabled=True,required=False, widget=forms.NumberInput(
        attrs={'class':'inputformsfill', 'id':'total_amount'}
    ))
    Current_EB_MTR_KWH = forms.CharField(required=False, widget=forms.NumberInput(
        attrs={'class':'inputformsfill'}
    ))
    Current_EB_PIU_Reading = forms.CharField(required=False, widget=forms.NumberInput(
        attrs={'class':'inputformsfill'}
    ))
    Remarks = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class':'inputformsfill'}
    ))
    Before_Fuel_CM_Photo = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class':'img-input'}
    ))
    After_Fuel_Filling_CM_Photo = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class':'img-input'}
    ))

    class Meta:
        model = EnergyFuel
        widgets = {
            'global_id': forms.Select(attrs={'class':'inputformsfill js-example-basic-single', 'name':'cars', 'id':'cars'}),
            'Tasks': forms.Select(attrs={'class':'inputformsfill', 'id':'tasks_id'}),
            'DG_HMR_Status': forms.Select(attrs={'class':'inputformsfill', 'id':'HMR_status'}),
            'DG_PIU_Status': forms.Select(attrs={'class':'inputformsfill', 'id':'status_PUI'}),
            'Diesel_Filling_Done': forms.Select(attrs={'class':'inputformsfill'}),
            'EB_Meter_Status': forms.Select(attrs={'class':'inputformsfill', 'id':'EBMeter_status'}),
            'EB_PIU_Meter_Status': forms.Select(attrs={'class':'inputformsfill', 'id':'EBPIU_Status'}),
            'DG_Serial_Number': forms.TextInput(attrs={'class':'inputformsfill'}),
            'Date_Of_Diesel_Filling': forms.DateInput(attrs={'class':'inputformsfill', 'type':'date'}),
            'FT_ID': forms.TextInput(attrs={'class':'inputformsfill'}),
            'FT_name': forms.TextInput(attrs={'class':'inputformsfill'}),
            'FT_mobile_no': forms.NumberInput(attrs={'class':'inputformsfill'}),
            'Receipt_No': forms.TextInput(attrs={'class':'inputformsfill'}),
            'Card_Number': forms.TextInput(attrs={'class':'inputformsfill'}),
            'Vehicle_Plate': forms.TextInput(attrs={'class':'inputformsfill'}),
        }
        fields = ['global_id','Tasks','DG_Serial_Number','DG_HMR_Status','DG_HMR_Reading','DG_PIU_Status','Current_DG_PIU_Reading',
                  'Diesel_Filling_Done','Date_Of_Diesel_Filling','Diesel_Balance_Before_Filling','Fuel_Qty_Filled',
                  'EB_Meter_Status','Current_EB_MTR_KWH','EB_PIU_Meter_Status','Current_EB_PIU_Reading', 'Total_DC_Load', 
                  'Total_EB_KWH_Reading_from_all_Channels','Remarks','FT_ID','FT_name','FT_mobile_no','Receipt_No','Card_Number',
                  'Vehicle_Plate','Before_Fuel_CM_Photo','After_Fuel_Filling_CM_Photo',]



class FuelDrawnFTForm(forms.ModelForm):
    Remarks = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class':'inputformsfill', 'id':'input_id_frm'}
    ))
    Total_Diesel_Cost_Rs = forms.CharField(disabled=True,required=False, widget=forms.TextInput(
        attrs={'class':'inputformsfill', 'id':'amount3', 'value':'0'}
    ))
    class Meta:
        model = FuelDrawn
        widgets = {
            'FT_ID': forms.TextInput(attrs={'class':'inputformsfill', 'id':'input_id_frm'}),
            'FT_name': forms.TextInput(attrs={'class':'inputformsfill', 'id':'input_id_frm'}),
            'FT_mobile_no': forms.TextInput(attrs={'class':'inputformsfill', 'id':'input_id_frm'}),
            'Cluster_Name': forms.Select(attrs={'class':'inputformsfill', 'id':'input_id_frm'}),
            'Fuel_Drawn_Date': forms.DateInput(attrs={'class':'inputformsfill', 'id':'input_id_frm', 'type':'date'}),
            'Card_No': forms.TextInput(attrs={'class':'inputformsfill', 'id':'input_id_frm'}),
            'City_Township_Fuel_Station': forms.TextInput(attrs={'class':'inputformsfill', 'id':'input_id_frm'}),                 
            'Customer': forms.Select(attrs={'class':'inputformsfill', 'id':'input_id_frm'}),
            'Fuel_Station_Name': forms.TextInput(attrs={'class':'inputformsfill', 'id':'input_id_frm'}),
            'Diesel_Purchased_Qty': forms.NumberInput(attrs={'class':'inputformsfill', 'id':'amount1'}),
            'Diesel_Per_Ltr_Cost_Rs': forms.NumberInput(attrs={'class':'inputformsfill', 'id':'amount2'}),                
            'Receipt_No': forms.TextInput(attrs={'class':'inputformsfill', 'id':'input_id_frm'}),                
            'Receipt_Image_Upload': forms.FileInput(attrs={'class':'img-input', 'id':'input_id_frm'}),
            'Vehicle_Plate':forms.TextInput(attrs={'class':'inputformsfill', 'id':'input_id_frm'}),
        }
        fields = ['FT_ID','FT_name','FT_mobile_no','Cluster_Name','Fuel_Drawn_Date','Card_No','City_Township_Fuel_Station',
                  'Customer','Fuel_Station_Name','Diesel_Purchased_Qty','Diesel_Per_Ltr_Cost_Rs','Total_Diesel_Cost_Rs',
                  'Receipt_No','Receipt_Image_Upload','Vehicle_Plate','Remarks']        
        