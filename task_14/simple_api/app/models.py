from django.db import models
class Server(models.Model):

    name = models.CharField('name', max_length=255)
    ip_address = models.GenericIPAddressField('IP', max_length=16, default='0.0.0.0')
    description = models.TextField('description', max_length=255, default='no_description')
    server_is_active = models.BooleanField('IS_active', default=False)

    class Meta:
        managed = True
        verbose_name = 'Server'

class AdditionalInformation(models.Model):

    host_information = models.JSONField(default = {})
    network = models.JSONField(default = {})
    disk = models.JSONField(default = {})
    memory = models.JSONField(default = {})
    cpu = models.JSONField(default = {})
    load_average = models.JSONField(default = {})
    battery_charge_percentage = models.JSONField(default = {})
    AC_power = models.JSONField(default = {})
