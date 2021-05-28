from django.db import models


class Role(models.Model):
    reserved_names = ('Директор', 'Управляющий', 'Бухгалтер', 'Электрик', 'Сантехник')

    name = models.CharField(
        max_length=50,
    )
    statistics = models.BooleanField(
        default=1,
    )
    account_transaction = models.BooleanField(
        default=1,
    )
    invoice = models.BooleanField(
        default=1,
    )
    account = models.BooleanField(
        default=1,
    )
    flat = models.BooleanField(
        default=1,
    )
    user = models.BooleanField(
        default=1,
    )
    house = models.BooleanField(
        default=1,
    )
    message = models.BooleanField(
        default=1,
    )
    master_request = models.BooleanField(
        default=1,
    )
    meter_readings = models.BooleanField(
        default=1,
    )
    site_control = models.BooleanField(
        default=1,
    )
    services = models.BooleanField(
        default=1,
    )
    tariffs = models.BooleanField(
        default=1,
    )
    roles = models.BooleanField(
        default=1,
    )
    user_admin = models.BooleanField(
        default=1,
    )
    pay_company = models.BooleanField(
        default=1,
    )

    def __str__(self):
        return self.name

    def get_available_url_pattern_by_role(self):
        if self.statistics:
            return 'admin_panel:statistics'
        elif self.user:
            return 'admin_panel:users_list'
        elif self.account_transaction:
            return 'admin_panel:account_transactions_list'
        elif self.house:
            return 'admin_panel:houses_list'
        elif self.flat:
            return 'admin_panel:flats_list'
        elif self.site_control:
            return 'admin_panel:index'
        elif self.services:
            return 'admin_panel:services_list'
        elif self.tariffs:
            return 'admin_panel:tariff_list'
        elif self.roles:
            return 'admin_panel:role_list'
        elif self.user_admin:
            return 'admin_panel:users_admin_list'
        elif self.pay_company:
            return 'admin_panel:pay_company'
        else:
            return 'website:index'
