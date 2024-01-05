from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

DEPARTMENTS = (
    ('None','None'),
    ('HR','HR'),
    ('IT','IT'),
    ('Accounts','Accounts'),
    ('CAD','CAD'),
    ('SCM','SCM'),
    ('Technical','Technical'),
)

class UserBaseManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=200, unique=True)
    department = models.CharField(max_length=50, choices=DEPARTMENTS)
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserBaseManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{str(self.first_name)} {str(self.last_name)} : {str(self.username)}'

    def has_perm(self, perms, obj=None):
        return self.is_admin
    
    def has_module_perms(self, abel_app):
        return True
    


class SiteFixed(models.Model):
    global_id = models.CharField(verbose_name='global ID', max_length=7, primary_key=True)
    site_name = models.CharField(verbose_name='Site Name', max_length=100)
    site_address = models.TextField(verbose_name='Site Address')
    cluster = models.CharField(verbose_name='Cluster', max_length=100)
    CE = models.CharField(verbose_name='SE', max_length=250)
    site_tenancy = models.CharField(verbose_name='Site Tenancy',max_length=250)
    DG_NON_DG = models.CharField(verbose_name='DG / Non DG', max_length=20)
    DG_capacity_kva = models.CharField(verbose_name='DG Capacity (Kva)', max_length=100)
    EB_status = models.CharField(verbose_name='EB Status', max_length=50)
    card_number = models.CharField(verbose_name='Card Number', max_length=100)
    last_month_approved_CPH = models.CharField(verbose_name='Last Month Approved CPH')

    def __str__(self):
        return str(self.global_id)
    


IS_YES_OR_NO = (
    ('Yes','Yes'),
    ('No','No'),
)

WORKING_NOTWORKING = (
    ('Working','Working'),
    ('Not-Working','Not-Working'),
    ('Missing','Missing'),
)

TASKS = (
    ('Energy Reading and Diesel Filling','Energy Reading and Diesel Filling'),
    ('Energy Reading','Energy Reading'),
)

class EnergyFuel(models.Model):
    global_id = models.ForeignKey(SiteFixed, on_delete=models.CASCADE)
    Tasks = models.CharField(verbose_name='Tasks', max_length=50, choices=TASKS)
    DG_Serial_Number = models.TextField(verbose_name='DG Serial Number')
    DG_HMR_Status = models.CharField(verbose_name='DG HMR Status', max_length=30, choices=WORKING_NOTWORKING)
    DG_HMR_Reading = models.IntegerField(verbose_name='DG HMR Reading')
    DG_PIU_Status = models.CharField(verbose_name='DG PIU Status', max_length=30, choices=WORKING_NOTWORKING)
    Current_DG_PIU_Reading = models.IntegerField(verbose_name='Current DG PIU Reading')
    Diesel_Filling_Done = models.CharField(verbose_name='Diesel Filling Done', max_length=20, choices=IS_YES_OR_NO)
    Date_Of_Diesel_Filling = models.DateField(verbose_name='Date of Diesel Filling')
    Diesel_Balance_Before_Filling = models.IntegerField(verbose_name='Diesel Balance Before Filling')
    Fuel_Qty_Filled = models.IntegerField(verbose_name='Fuel Qty. Filled')
    Current_Diesel_Balance = models.IntegerField(verbose_name='Current Diesel Balance')
    EB_Meter_Status = models.CharField(verbose_name='EB Meter Status', max_length=30, choices=WORKING_NOTWORKING)
    Current_EB_MTR_KWH = models.IntegerField(verbose_name='Current EB MTR (KWH)')
    EB_PIU_Meter_Status = models.CharField(verbose_name='EB PIU Meter Status', max_length=30, choices=WORKING_NOTWORKING)
    Current_EB_PIU_Reading = models.IntegerField(verbose_name='Current EB PIU Reading')
    Total_DC_Load = models.IntegerField(verbose_name='Total DC Load')
    Total_EB_KWH_Reading_from_all_Channels = models.IntegerField(verbose_name='Total EB KWH Reading from all channels')
    Remarks = models.TextField(verbose_name='Remarks')
    FT_ID = models.CharField(verbose_name='FT ID', max_length=50)
    FT_name = models.CharField(verbose_name='FT Name', max_length=200)
    FT_mobile_no = models.CharField(verbose_name='FT Mobile No', max_length=10)
    Receipt_No = models.CharField(verbose_name='Receipt Number', null=True, max_length=200)
    Card_Number = models.CharField(verbose_name='Card Number', null=True, max_length=200)
    Vehicle_Plate = models.CharField(verbose_name='Vehicle Plate', null=True, max_length=200)
    Before_Fuel_CM_Photo = models.ImageField(verbose_name='Before Fuel (CM) Photo', upload_to='Before Fuel Filling (CM)/%y')
    After_Fuel_Filling_CM_Photo = models.ImageField(verbose_name='After Fuel Filling(CM) Photo', upload_to='After Fuel Filling (CM)/%y')
    DG_Running_HRS = models.TextField(verbose_name='DG Running Hrs')
    CPH_CPH_Comparison_With_Last_CPH = models.TextField(verbose_name='CPH CPH Comparioson with Approved')
    CPH = models.TextField(verbose_name='CPH')	
    EB_KWH = models.TextField(verbose_name='EB KWH')

    def __str__(self):
        return str(self.global_id.global_id)
    




CLUSTERS = (
    ('Balasore','Balasore'),
    ('Baripada','Baripada'),
    ('Berhampur','Berhampur'),
    ('Bhadrak','Bhadrak'),
    ('Bhubaneswar','Bhubaneswar'),
    ('Cuttack','Cuttack'),
    ('Paradeep','Paradeep'),
    ('Puri','Puri'),
    ('Rouekela','Rouekela'),
    ('Sambalpur','Sambalpur'),
)

CUSTOMERS = (
    ('ATC','ATC'),
    ('JIO','JIO'),
)

class FuelDrawn(models.Model):
    FT_ID = models.CharField(verbose_name='FT ID', max_length=50)
    FT_name = models.CharField(verbose_name='FT Name', max_length=200)
    FT_mobile_no = models.CharField(verbose_name='FT Mobile No', max_length=10)
    Cluster_Name = models.CharField(verbose_name='Cluster Name', max_length=50, choices=CLUSTERS)
    Fuel_Drawn_Date = models.DateField(verbose_name='Fuel Drawn Date')
    Card_No = models.TextField(verbose_name='Booklet No. / Card No.')
    City_Township_Fuel_Station = models.TextField(verbose_name='City /Township (Fuel Station)')
    Customer = models.CharField(verbose_name='Customer', max_length=20, choices=CUSTOMERS)
    Fuel_Station_Name = models.TextField(verbose_name='Fuel Station Name')
    Diesel_Purchased_Qty = models.IntegerField(verbose_name='Diesel Purchased Qty. (Liters)')
    Diesel_Per_Ltr_Cost_Rs = models.IntegerField(verbose_name='Diesel Per Ltr. Cost. Rs.')
    Total_Diesel_Cost_Rs = models.IntegerField(verbose_name='Total Diesel Cost Rs.')
    Receipt_No = models.TextField(verbose_name='Receipt No')
    Receipt_Image_Upload = models.ImageField(verbose_name='Receipt Image Upload', upload_to='Receipt Image Upload/%y')
    Vehicle_Plate = models.TextField(verbose_name='Vehicle Plate')
    Remarks = models.TextField(verbose_name='Remarks')


    def __str__(self):
        return str(self.FT_ID)