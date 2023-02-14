from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify
# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    olusturan = models.ForeignKey(User, on_delete=models.CASCADE)
    isim = models.CharField(max_length=100)
    resim = models.FileField(upload_to='profiller/')
    olusturulmaTarihi = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, editable=False)
    def __str__(self):
        return self.isim

    def save(self):
        self.slug = slugify(self.isim.replace('ı','i'))
        super(Profile, self).save()

# bu profilin kime ait olduğu


class Hesap(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resim = models.FileField(upload_to='hesaplar/')
    tel = models.IntegerField()

    def __str__(self):
        return self.user.username