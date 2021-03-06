from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser

from register.managers import *


def get_profile_image_filepath(self):
    return f'profile_images/{self.pk}/{"profile_image.png"}'


def get_default_profile_image():
    return 'default_profile_image.png'


class AbstractUser(AbstractBaseUser):
    """
    AbstractUser model is a base form other user model
    and contain register/login logic.
    """
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True,
    )
    date_joined = models.DateField(
        verbose_name='date joined',
        auto_now_add=True,
    )
    last_login = models.DateTimeField(
        verbose_name='last login',
        auto_now=True,
    )
    is_admin = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_superuser = models.BooleanField(
        default=False,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    class Meta:
        abstract = True
        ordering = ('-id',)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class User(AbstractUser):
    """
    Custom User model to register and
    login users in application.
    """
    STATUS = (
        ('Активен', 'Активен'),
        ('Новый', 'Новый'),
        ('Отключен', 'Отключен')
    )
    ROLE = (
        ('Владелец квартиры', 'Владелец квартиры'),
        ('Директор', 'Директор'),
        ('Управляющий', 'Управляющий'),
        ('Бухгалтер', 'Бухгалтер'),
        ('Электрик', 'Электрик'),
        ('Сантехник', 'Сантехник'),
    )

    first_name = models.CharField(
        verbose_name='first name',
        max_length=50,
        default='',
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=50,
        default='',
        blank=True,
    )
    middle_name = models.CharField(
        verbose_name='middle name',
        max_length=50,
        default='',
        blank=True,
    )
    full_name = models.CharField(
        verbose_name='full name',
        max_length=155,
        blank=True,
    )
    phone = PhoneNumberField(
        verbose_name='phone number',
        max_length=25,
        default='',
        blank=True,
    )
    telegram = models.CharField(
        verbose_name='telegram',
        max_length=100,
        default='',
        blank=True,
    )
    viber = models.CharField(
        verbose_name='viber',
        max_length=100,
        default='',
        blank=True,
    )
    notes = models.TextField(
        verbose_name='notes about',
        max_length=1500,
        default='',
        blank=True,
    )
    birth_date = models.DateField(
        verbose_name='date joined',
        null=True,
        blank=True,
    )
    status = models.CharField(
        verbose_name='status of the user',
        max_length=100,
        blank=True,
        null=True,
        default=STATUS[1][0],
        choices=STATUS,
    )
    role = models.CharField(
        verbose_name='role of the user',
        max_length=150,
        blank=True,
        null=True,
        default=ROLE[0][0],
        choices=ROLE,
    )
    image = models.ImageField(
        blank=True,
        upload_to='images/users/user_image/',
        verbose_name='Сменить изображение',
    )

    objects = CustomUserManager()
    users_admin = UserAdminManager()
    users = OwnersManager()

    def __str__(self):
        if self.is_staff:
            return f'{self.role} - {self.full_name}'
        else:
            return self.full_name

    @classmethod
    def get_users_list(cls):
        return cls.objects.filter(is_staff=False)

    @classmethod
    def get_active_users(cls):
        return cls.objects.filter(status='Активен', is_staff=False)

    @classmethod
    def get_users_admin_list(cls):
        return cls.objects.filter(is_staff=True)

    @classmethod
    def get_users_count(cls):
        return cls.objects.filter(is_staff=False).count()

    @classmethod
    def get_users_admin_count(cls):
        return cls.objects.filter(is_staff=True).count()

    @classmethod
    def get_user_by_pk(cls, pk):
        return cls.objects.get(pk=pk)
