from django.contrib import admin
from .models import Feedback, gallery

# Register your models here.
admin.site.register(Feedback)
# admin.site.register(Enquiry)
# admin.site.register(gallery)

@admin.register(gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'img']


