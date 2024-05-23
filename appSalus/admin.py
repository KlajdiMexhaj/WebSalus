from pyexpat import model
from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin
from ckeditor.widgets import CKEditorWidget
from parler.admin import TranslatableAdmin

# Register your models here.

class MyModelAdmin(AdminVideoMixin,admin.ModelAdmin):
     list_filter = ['departamenti']
     list_display = ['get_name', 'departamenti']
     list_display_links = ['get_name', 'departamenti']
     search_fields = ['translations__name']

     def get_name(self, obj):
        return obj.name  # Access translated name

     get_name.short_description = 'Name'
class MjeketAdmin( MyModelAdmin, TranslatableAdmin):
     pass
admin.site.register(Mjeket,MjeketAdmin)
admin.site.register(Departamenti, TranslatableAdmin)
admin.site.register(Specialitet, TranslatableAdmin)
admin.site.register(CheckUp)
admin.site.register(About, TranslatableAdmin)
admin.site.register(Foto)
admin.site.register(KlinikaFerti, TranslatableAdmin)
admin.site.register(AeMC, TranslatableAdmin)

class ArtikujtAdmin(admin.ModelAdmin):
     list_filter = ['departamenti']
     list_display = ['name','departamenti']
     list_display = ['name','departamenti']
     search_fields = ['name']
     
     

class ArtikujtInformuesAdmin(ArtikujtAdmin, TranslatableAdmin):
    pass
admin.site.register(artikujtinformues,ArtikujtInformuesAdmin)


admin.site.register(artikujtinformuesAeMC, TranslatableAdmin)
admin.site.register(artikujtinformuesKartaInSalus, TranslatableAdmin)
admin.site.register(artikujtinformuesDonnaSalus, TranslatableAdmin)
admin.site.register(Kontakt_Salus)
class LiniTakim_salus_admin(admin.ModelAdmin):
    list_display = ['name','published_at']
    list_display_links = ['name','published_at']
admin.site.register(LiniTakim_salus,LiniTakim_salus_admin)
admin.site.register(Kontact_Salus_Tirana)
admin.site.register(Kontact_Salus_Laborator)
admin.site.register(Video_AlbaNostra)
admin.site.register(artikujtinformuesAlbaNostra, TranslatableAdmin)


