from django.db import models
from django.forms import ValidationError

# Create your models here.

# class Nav(models.Model):
#     nav_title = models.CharField(max_length=255)
#     nav_btn_url = models.CharField(max_length=255)

#     class Meta:
#         ordering = ('nav_title',)
#         verbose_name_plural = 'Nav Content'

#     def __str__(self):
#         return self.nav_title

class SingletonModel(models.Model):
    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError('There can be only one instance of this model.')
        return super(SingletonModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Hero(SingletonModel):
    hero_title = models.CharField(max_length=255)
    hero_content = models.CharField(max_length=255)
    button_url = models.CharField(max_length=255)
    button_title = models.CharField(max_length=255, default='Explore Now')
    bg_video = models.FileField(upload_to='pageFiles/Videos', blank=True, null=True)
    bg_img = models.ImageField(upload_to='pageFiles/images', blank=True, null=True)

    class Meta:
        ordering = ('hero_title',)
        verbose_name_plural = 'Hero Content'

    def __str__(self):
        return self.hero_title

    def clean(self):
        # Ensure either bg_img or bg_video is set, but not both
        if self.bg_img and self.bg_video:
            raise ValidationError(('Only one of background image or background video can be set.'))

        if not self.bg_img and not self.bg_video:
            raise ValidationError(('Either background image or background video must be set.'))

        # Call the super clean method to ensure model's own validation
        super().clean()
    
class Ab_list(models.Model):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'About list'

    def __str__(self):
        return self.title
    
class Ab_img(models.Model):
    alt = models.CharField(max_length=255)
    img = models.ImageField(upload_to='pageFiles/images', blank=True, null=True)

    class Meta:
        ordering = ('alt',)
        verbose_name_plural = 'About images'

    def __str__(self):
        return self.alt
    
class About(SingletonModel):
    about_title = models.CharField(max_length=255)
    about_content = models.TextField(null=True, blank=True)
    ab_list = models.ManyToManyField('Ab_list', blank=True)
    ab_img = models.ManyToManyField('Ab_img', blank=True)

    class Meta:
        ordering = ('about_title',)
        verbose_name_plural = 'About Content'

    def __str__(self):
        return self.about_title
    
class Showcase(models.Model):
    alt = models.CharField(max_length=255)
    img = models.ImageField(upload_to='pageFiles/images', blank=True, null=True)

    class Meta:
        ordering = ('alt',)
        verbose_name_plural = 'Showcase Images'

    def __str__(self):
        return self.alt

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    ans = models.TextField()

    class Meta:
        ordering = ('question',)
        verbose_name_plural = 'FAQ'

    def __str__(self):
        return self.question
    
class CTA(SingletonModel):
    cta_title = models.CharField(max_length=255)
    cta_content = models.TextField(null=True, blank=True)
    cta_btn_url = models.CharField(max_length=255, blank=True, null=True)
    cta_btn_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('cta_title',)
        verbose_name_plural = 'CTA'

    def __str__(self):
        return self.cta_title
    
class Rev(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()
    img = models.ImageField(upload_to='pageFiles/reviweimages', blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    highlight = models.CharField(max_length=500)
    img = models.ImageField(upload_to='pageFiles/blogimages', blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Blog posts'

    def __str__(self):
        return self.title
    
class Socials(models.Model):
    name = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Socials Icons'

    def __str__(self):
        return self.name

class Support(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='pageFiles/supportimages', null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Support Images'

    def __str__(self):
        return self.name
    
class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.name

class Contacts(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Contact list'

    def __str__(self):
        return self.name

class Map(models.Model):
    location = models.CharField(max_length=255)
    iFrame_link =models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('location',)
        verbose_name_plural = 'Map'
    
    def __str__(self):
        return self.location