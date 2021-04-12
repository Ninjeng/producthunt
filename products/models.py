from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

def upload_location(instance, filename):
    file_path = 'product/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.product_name), filename=filename)
    return file_path

class Product(models.Model):
    product_name = models.CharField(max_length=500,blank=False,null=False)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    description = models.CharField(max_length=500,blank=False,null=False)
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)
    
    
    def __str__(self):
        return self.product_name

@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.author.username + "-" + instance.product_name + '-' + str(instance.author.id) + str(len(
                instance.description)))
        
pre_save.connect(pre_save_blog_post_receiver, sender=Product)