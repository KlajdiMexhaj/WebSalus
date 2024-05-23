from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from modeltranslation.translator import TranslationOptions, register
from modeltranslation.fields import TranslationField


  # # Create your models here.

class Departamenti(TranslatableModel):
    translations = TranslatedFields (
    name = models.CharField(max_length=200, blank=True,null=True)
    )
    

    class Meta:
        verbose_name = _("departamenti")
        verbose_name_plural = _("departamentet")

    def __str__(self):
        return self.name if self.name else "Unnamed Departamenti "



class Mjeket (TranslatableModel):
    departamenti= models.ForeignKey(Departamenti, related_name=_('mjeket_departamenti'), on_delete=models.SET_NULL,blank=True,null=True)
    translations= TranslatedFields(
    name = models.CharField(_('name'),max_length=100, blank=True,null=True),
    mjeket_arsimi = RichTextField(_('mjeket_arsimi'),blank=True,null=True),
    mjeket_punesimi = RichTextField(_('mjeket_punesimi'), blank=True,null=True),
    )
    mjeket_image = models.ImageField(upload_to='mjeket/', blank=True,null=True)
    mjeket_video = EmbedVideoField( blank=True,null=True)
    

    def __str__(self):
        return self.name if self.name else "Unnamed Mjeket"
    


class Specialitet (TranslatableModel):
    translations= TranslatedFields(
    name = models.CharField(max_length=100, blank=True,null=True),
    specialitet_pershkrimi = RichTextField(blank=True,null=True),
    specialitet_serviset = RichTextField( blank=True,null=True),
    )
    specialitet_image = models.ImageField(upload_to='specialitet', blank=True,null=True)
    
    specialitet_video = EmbedVideoField( blank=True,null=True)
    specialitet_video = EmbedVideoField( blank=True,null=True)
    specialitet_video1 = EmbedVideoField( blank=True,null=True)
    specialitet_video2 = EmbedVideoField( blank=True,null=True)
    specialitet_video3 = EmbedVideoField( blank=True,null=True)
    specialitet_video4 = EmbedVideoField( blank=True,null=True)
    specialitet_video5 = EmbedVideoField( blank=True,null=True)
    specialitet_video6 = EmbedVideoField( blank=True,null=True)
    specialitet_video7 = EmbedVideoField( blank=True,null=True)
    specialitet_video8 = EmbedVideoField( blank=True,null=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Specialitet"





class CheckUp (models.Model):
    check_up = models.ImageField(upload_to='checkup', blank=True,null=True)
    check_name = models.CharField(max_length=100, blank=True,null=True)
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published_at']


    def __str__(self):
        return self.check_name
    



class About (TranslatableModel):
    about_img = models.ImageField(upload_to='aboutus')
    translations = TranslatedFields (
    about_pershkrimi = RichTextField( blank=True,null=True),
    about_oltipershkrimi = RichTextField( blank=True,null=True),
    )
    about_imgambjeti = models.ImageField(upload_to='aboutus', blank=True,null=True)



class Foto (models.Model):
    foto_img = models.ImageField(upload_to="foto_ambjete", blank=True,null=True)







class KlinikaFerti(TranslatableModel):
    translations= TranslatedFields(
    klinika_name=models.CharField(max_length= 100, blank=True,null=True),
    klinika_description= RichTextField(blank=True,null=True),
    )
    klinika_img = models.ImageField(upload_to='klinikafer',blank=True,null=True)
    


    def __str__(self):
        return self.klinika_name  if self.klinika_name else "Unnamed KlinikaFerti"



class AeMC(TranslatableModel):
    translations= TranslatedFields(
    AeMC_text = RichTextField(blank=True,null=True),
    AeMC_CV = RichTextField(blank = True,null=True),
)





class artikujtinformues(TranslatableModel):
    
    departamenti= models.ForeignKey(Departamenti, related_name=_('departamenti'), on_delete=models.SET_NULL,blank=True,null=True)
    translations = TranslatedFields (
    name= models.CharField(_('name'),max_length=100,blank=True,null=True),
    art_description = RichTextField(_('art_description'),blank=True,null=True),
    )
    image = models.ImageField(upload_to='artikujtinformues/',blank=True,null=True)
    
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.name if self.name else "Unnamed Artikujtinformues"



class artikujtinformuesAeMC(TranslatableModel):
    translations = TranslatedFields (
    name = models.CharField( max_length=100, blank=True, null=True),
    artAeMC = RichTextField( blank=True, null=True),
    )
    image = models.ImageField(upload_to='artikujtinformuesAeMC/', blank=True, null=True)

    

    
    published_at = models.DateTimeField( default=timezone.now)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.name if self.name else "Unnamed ArtikujtInformuesKartaInSalus"



class artikujtinformuesKartaInSalus(TranslatableModel):
    translations = TranslatedFields(
    name = models.CharField(_('name'),max_length=100,blank=True,null=True),
    art_KartaInSalus = RichTextField(_('art_KartaInSalus'),blank=True,null=True),
    )
    image = models.ImageField(upload_to="artikujtinformuesKartaInSalus/",blank=True,null=True)
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published_at']
        
    def __str__(self):
        return self.name if self.name else "Unnamed ArtikujtInformuesKartaInSalus"
    


class artikujtinformuesDonnaSalus(TranslatableModel):
    translations = TranslatedFields(
    name = models.CharField(max_length=100,blank=True,null=True),
    art_DonnaSalus = RichTextField(blank=True,null=True),
    )
    image = models.ImageField(upload_to='artikujtinformuesDonnaSalus/',blank=True,null=True)
    
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.name if self.name else "Unnamed ArtikujtInformuesDonnaSalus"
    


class Kontakt_Salus(models.Model):
    fullname = models.CharField(max_length=50,blank=True,null=True)
    number = models.CharField(max_length=50,blank=True,null=True)
    message = models.TextField(max_length=2000,blank=True,null=True)

    def __str__(self):
        return self.fullname


class LiniTakim_salus(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True)
    email= models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=50,blank=True,null=True)
    specialiteti = models.CharField(max_length=50,blank=True,null=True)
    mjeku = models.CharField(max_length=50,blank=True)
    sms = models.TextField(max_length=2000,null=True,blank=True)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Kontact_Salus_Tirana(models.Model):
    name= models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    message = models.TextField(max_length=2000,null=True,blank=True)

    def __str__(self):
        return self.name
    

class Kontact_Salus_Laborator(models.Model):
    name= models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    message = models.TextField(max_length=2000,null=True,blank=True)

    def __str__(self):
        return self.name
    

class Video_AlbaNostra(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    url = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title


class artikujtinformuesAlbaNostra(TranslatableModel):
    
    
    translations = TranslatedFields (
    name= models.CharField(_('name'),max_length=100,blank=True,null=True),
    art_description = RichTextField(_('art_description'),blank=True,null=True),
    )
    image = models.ImageField(upload_to='artikujtinformuesAlbaNostra/',blank=True,null=True)
    
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.name if self.name else "Unnamed ArtikujtinformuesAlbaNostra"