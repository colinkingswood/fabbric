from django.db import models


# to extend this it would probably be worth moving the image to a separate model and we could have
# mutiple images per item, side views, from behind
class ClothingItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clothing/')
    color = models.CharField(max_length=16, default='white')  # todo validate this to hex or RGB
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]



