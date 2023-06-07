
from datetime import timedelta
from email.policy import default
from enum import auto
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


def in_three_days():
    return timezone.now() + timedelta(days=90)


class company(models.Model):
    company_logo = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    company_country = models.CharField(max_length=50, blank=True, null=True)
    company_state = models.CharField(max_length=50, blank=True, null=True)
    company_zip_code = models.CharField(max_length=50, blank=True, null=True)
    company_location = models.CharField(max_length=50, blank=True, null=True)
    user_email = models.CharField(max_length=50, blank=True, null=True)
    user_login = models.CharField(max_length=50, blank=True, null=True)
    company_website = models.CharField(max_length=50, blank=True, null=True)
    company_info = models.CharField(max_length=50, blank=True, null=True)
    is_public = models.CharField(max_length=50, blank=True, null=True)
    company_slogan = models.CharField(max_length=50, blank=True, null=True)
    group_image = models.CharField(max_length=50, blank=True, null=True)
    remote_ready = models.CharField(max_length=50, blank=True, null=True)
    company_size = models.CharField(max_length=50, blank=True, null=True)
    twitter_link = models.CharField(max_length=50, blank=True, null=True)
    linkedin_link = models.CharField(max_length=50, blank=True, null=True)
    facebook_link = models.CharField(max_length=50, blank=True, null=True)
    field_8 = models.CharField(max_length=50, blank=True, null=True)
    field_5 = models.CharField(max_length=50, blank=True, null=True)
    field_6 = models.CharField(max_length=50, blank=True, null=True)
    field_7 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.company_name




class Jobs(models.Model):
    company = models.ForeignKey(company, verbose_name=(
        "company"), on_delete=models.DO_NOTHING, blank=True, null=True)

    job_title = models.CharField(max_length=100, blank=True, null=True)
    

    is_approved = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_filled = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    job_country = models.CharField(max_length=50, blank=True, null=True)
    job_state = models.CharField(max_length=50, blank=True, null=True)
    job_zip_code = models.CharField(max_length=50, blank=True, null=True)
    job_city = models.CharField(max_length=50, blank=True, null=True)
    job_address = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    job_created_at = models.DateTimeField(blank=True, null=True)
    job_expires_at = models.DateField(default=in_three_days)
    company_website = models.URLField()
    job_description = models.TextField(unique=True)
    wpjobboard_am_data = models.URLField()
    company_url = models.URLField()
    company_name = models.CharField(max_length=50, blank=True, null=True)
    company_email = models.EmailField()
    company_logo = models.ImageField()
    company_country = models.CharField(max_length=50, blank=True, null=True)
    company_state = models.CharField(max_length=50, blank=True, null=True)
    company_zip_code = models.CharField(max_length=50, blank=True, null=True)
    company_location = models.CharField(max_length=50, blank=True, null=True)
    company_info = models.CharField(max_length=50, blank=True, null=True)
    is_public = models.CharField(max_length=50, blank=True, null=True)
    company_slogan = models.CharField(max_length=50, blank=True, null=True)
    remote_ready = models.CharField(max_length=50, blank=True, null=True)
    company_size = models.CharField(max_length=50, blank=True, null=True)
    twitter_link = models.URLField()
    linkedin_link = models.URLField()
    facebook_link = models.URLField()
    job_description_format = models.CharField(max_length=50, default='html')

    def __str__(self):
        return self.job_title




@receiver(post_save, sender=Jobs)
def create_user_profile(sender, instance, created, **kwargs):
    company_name=instance.company_name
    company_email=instance.company_email
    company_country=instance.company_country
    company_state=instance.company_state
    company_zip_code=instance.company_zip_code
    company_location=instance.company_location
    company_info=instance.company_info
    is_public=instance.is_public
    user_login=company_email
    company_slogan=instance.company_slogan
    remote_ready=instance.remote_ready
    company_size=instance.company_size
    twitter_link=instance.twitter_link
    linkedin_link=instance.linkedin_link
    facebook_link=instance.facebook_link
    company_website=instance.company_url
    company_name=instance.company_name
    company_logo=instance.company_logo

    if created:
        data=company.objects.create(
            company_country=company_country,
            company_state=company_state,
            company_zip_code=company_zip_code,
            company_location=company_location,
            company_info=company_info,
            is_public=is_public,
            company_slogan=company_slogan,
            remote_ready=remote_ready,
            company_size=company_size,
            twitter_link=twitter_link,
            linkedin_link=linkedin_link,
            facebook_link=facebook_link,
            company_website=company_website,
            company_name=company_name,
            user_email=company_email,
            user_login=company_website,

            company_logo=company_logo,)
        instance.company=data
        instance.save()
