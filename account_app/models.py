from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from time import strftime, localtime, time


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('请输入邮箱地址')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            created_at=strftime("%Y-%m-%d %H:%M:%S", localtime(time())),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=email, username=username, password=password)
        user.is_admin = True
        user.save(using=self.db)
        return user


class MyUser(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True, auto_created=10001)
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        null=False,
    )
    phone = models.CharField(max_length=13)
    sex = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Buyer(models.Model):
    buyer_id = models.OneToOneField("MyUser", to_field='user_id', on_delete=models.CASCADE)
    cardNum = models.CharField(max_length=64)
    nickName = models.CharField(max_length=32)
    isActive = models.BooleanField()


class CustomerService(models.Model):
    customerService_id = models.OneToOneField("MyUser", to_field='user_id', on_delete=models.CASCADE)
    staff_id = models.AutoField(primary_key=True, auto_created=101)


class Seller(models.Model):
    seller_id = models.OneToOneField("MyUser", to_field='user_id', on_delete=models.CASCADE)
    shopName = models.CharField(primary_key=True, max_length=32)
    desc = models.CharField(max_length=255)
    isActive = models.BooleanField()
