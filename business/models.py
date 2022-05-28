# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Create your models here.
class MyManage(BaseUserManager):
    def create_user(self,email,name,want_to,contact,password=None):
       
        if not school_email:
            raise ValueError('Users must have a email')

        user = self.model(
        	name=name,
            email=self.normalize_email(email),
            want_to=want_to,
            contact=contact
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,want_to,contact,password=None):
        
        user = self.create_user(
            email,
            name=name,
            password=password,
            want_to=want_to,
            contact=contact
                  )
        user.is_admin = True
        user.save(using=self._db)
        return user

class record(AbstractBaseUser):
	name=models.CharField(max_length=15,unique=True)
	email=models.EmailField(unique=True)
	contact=models.CharField(max_length=10,default=0)
	want_to=models.CharField(max_length=10)
	is_activate=models.BooleanField(default=True)
	is_admin=models.BooleanField(default=False)

	objects=MyManage()

	USERNAME_FIELD='email'
	REQUIRED_FIELD=[]
	

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def __str__(self):
		return self.email


	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		return self.is_admin


class product(models.Model):
	seller=models.CharField(max_length=15,default=None)
	name=models.CharField(max_length=15)
	price=models.IntegerField()
	details=models.CharField(max_length=15)


