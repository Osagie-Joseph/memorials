from django.db import models


# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    message = models.TextField(max_length=None)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'People contacting us'


class ConDetails(models.Model):
    address = models.TextField(max_length=None)
    email = models.EmailField()
    our_current_number = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = 'Our Contact Details'

# TODO you need to create a google and facebook Application programming interface and
# TODO you need to login to the admin site via localhost8000/admin and
#  input your API secret key browse if you get confused


# TODO https://console.developers.google.com/ that the url to get social account API for Google
# Todo https://developers.facebook.com/ that the url to get social account API for facebook


class Memorial(models.Model):
    thumbnail = models.ImageField()
    name = models.CharField(max_length=30)
    overview = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Someone\'s Memorial'
        verbose_name_plural = 'People Memorials'
