from django.db import models
from cloudinary.models import CloudinaryField

class Task(models.Model):
    العنوان = models.CharField(
        max_length=255,
        verbose_name="عنوان المهمة",
        null=True,
        blank=True
    )
    الوصف = models.TextField(
        verbose_name="وصف المهمة",
        null=True,
        blank=True
    )
    مكتملة = models.BooleanField(
        default=False,
        verbose_name="هل اكتملت؟"
    )
    الصورة = CloudinaryField(
        verbose_name="صورة المهمة",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.العنوان or "مهمة بدون عنوان"
