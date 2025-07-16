from django.db import models
from django.contrib.auth.models import AbstractUser


class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    username = None

    full_name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    JOB_CHOICES = [
        ('not_chosen', 'انتخاب کنید'),
        ('student', 'دانشجو'),
        ('engineer', 'مهندس'),
        ('teacher', 'معلم'),
        ('doctor', 'پزشک'),
        ('nurse', 'پرستار'),
        ('lawyer', 'وکیل'),
        ('artist', 'هنرمند'),
        ('programmer', 'برنامه‌نویس'),
        ('accountant', 'حسابدار'),
        ('manager', 'مدیر'),
        ('driver', 'راننده'),
        ('worker', 'کارگر'),
        ('clerk', 'کارمند اداری'),
        ('shopkeeper', 'فروشنده'),
        ('freelancer', 'فریلنسر'),
        ('retired', 'بازنشسته'),
        ('unemployed', 'بیکار'),
        ('other', 'سایر'),
    ]
    job = models.CharField(max_length=20, choices=JOB_CHOICES)
    EDUCATION_CHOICES = [
        ('not_chosen', 'انتخاب کنید'),
        ('cycle', 'سیکل'),
        ('diploma', 'دیپلم'),
        ('bachelor', 'لیسانس'),
        ('master', 'فوق لیسانس'),
        ('phd', 'دکتری'),
        ('postdoc', 'پسا دکتری'),
    ]
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES, default='master')
    email = models.EmailField()
    # password = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    mobile_number = models.CharField(max_length=11,unique=True)
    telephone_number = models.CharField(max_length=11)
    postal_code = models.CharField(max_length=10)
    full_address = models.TextField()
    is_designer = models.BooleanField(default=False)
    national_code = models.CharField(max_length=10, blank=True, null=True)

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['full_name', 'email','password']

    def __str__(self):
        return self.full_name


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    credit_balance = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    designs_count = models.PositiveIntegerField(default=0)
    orders_count = models.PositiveIntegerField(default=0)
    followers = models.ManyToManyField(CustomUser, related_name='following', blank=True)

    def __str__(self):
        return f"{self.user.full_name}"

# class DesignerProfile(models.Model):
#
