from __future__ import unicode_literals
from tabnanny import verbose

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

from model_utils import Choices

TYPE_USER = Choices(
    ("admin", "Administrador"),
    ("customer", "Cliente"),
    ("company", "Empresa")
)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_admin = models.BooleanField(
        _('admin status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )  
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    type = models.CharField(
        max_length=20, default="customer", choices=TYPE_USER
    )
    objects = UserManager(type="admin, customer, teacher")

    is_staff = models.BooleanField(
        default=True,
        help_text=_("Designates whether the user can log into this admin site."),
        verbose_name=_("Acesso ao Dashboard?"),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
''''
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
'''


class CustomerManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=TYPE_USER.customer)


class Customer(User):
    objects =  CustomerManager(type=TYPE_USER.customer)

    class Meta:
        proxy = True
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = TYPE_USER.customer
            self.is_superuser = False
            self.is_staff = True
        super().save(*args, **kwargs)


class CompanyManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type=TYPE_USER.company)

class Company(User):
    objects =  CompanyManager(type=TYPE_USER.company)

    class Meta:
        proxy = True
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = TYPE_USER.company
            self.is_superuser = False
            self.is_staff = True
        super().save(*args, **kwargs)