from django.db import models


class Basic(models.Model):
    created_date = models.DateTimeField(
        auto_now=True,
        verbose_name='زمان ثبت نام'
    )

    class Meta:
        abstract = True