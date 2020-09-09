from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils import timezone

class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(User=instance)
        

class evidencijagospodarstva(models.Model):
    id = models.AutoField(primary_key=True)
    katastar = models.CharField(max_length=120)
    naselje = models.CharField(max_length=50)
    povrsina = models.IntegerField()
    naziv_gosp = models.CharField(max_length=30)
    User_id= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
   

    def __str__(self):
        return self.naziv_gosp

class berba(models.Model):
    id = models.AutoField(primary_key=True)
    vrstamaslina = models.CharField(max_length=120)
    datumb = models.DateField(auto_now=False, auto_now_add=False)
    katcest = models.CharField(max_length=120)
    kolicinaubrano = models.DecimalField(max_digits=10, decimal_places=2)
    doprinosulja = models.DecimalField(max_digits=10, decimal_places=2)
    evidencijagospodarstva_id = models.ForeignKey(evidencijagospodarstva, on_delete=models.CASCADE)     

    def __str__(self):
        return self.vrstamaslina

class podaci_radnje(models.Model):
    id = models.AutoField(primary_key=True)
    vrstaradnje = models.CharField(max_length=120)
    katcest = models.CharField(max_length=120)
    datum = models.DateField(auto_now=False, auto_now_add=False)
    evidencijagospodarstva_id = models.ForeignKey(evidencijagospodarstva, on_delete=models.CASCADE)

    def __str__(self):
        return self.vrstaradnje

class prihranjivanje(models.Model):
    id = models.AutoField(primary_key=True)
    nazivprihrane = models.CharField(max_length=120)
    kolicinap = models.DecimalField(max_digits=10, decimal_places=2)
    katcest = models.CharField(max_length=120)
    datump = models.DateField(auto_now=False, auto_now_add=False)
    podaci_radnje_id = models.ForeignKey(podaci_radnje, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazivprihrane

class spricanje(models.Model):
    id = models.AutoField(primary_key=True)
    nazivtek = models.CharField(max_length=120)
    kolicina = models.DecimalField(max_digits=10, decimal_places=2)
    katcest = models.CharField(max_length=120)
    datums = models.DateField(auto_now=False, auto_now_add=False)
    podaci_radnje_id = models.ForeignKey(podaci_radnje, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazivtek

