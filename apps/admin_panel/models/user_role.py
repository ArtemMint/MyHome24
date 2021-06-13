from django.db import models


class UserRole(models.Model):
    name = models.CharField(max_length=255)
    statistic_status = models.BooleanField(default=0)
    account_transaction_status = models.BooleanField(default=0)
    invoice_status = models.BooleanField(default=0)
    account_status = models.BooleanField(default=0)
    flat = models.BooleanField(default=0)
    owners_status = models.BooleanField(default=0)
    house_status = models.BooleanField(default=0)
    message_status = models.BooleanField(default=0)
    master_request_status = models.BooleanField(default=0)
    meter_status = models.BooleanField(default=0)
    website_status = models.BooleanField(default=0)
    service_status = models.BooleanField(default=0)
    tariffs_status = models.BooleanField(default=0)
    role_status = models.BooleanField(default=0)
    user_status = models.BooleanField(default=0)
    pay_company_status = models.BooleanField(default=0)

    def __str__(self):
        return self.name
