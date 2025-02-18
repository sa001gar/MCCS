from django.contrib import admin
from .models import GalleryCategory, GalleryItem , Alumni, Notice

# Register your models here.
admin.site.register(GalleryCategory)
admin.site.register(GalleryItem)
admin.site.register(Alumni)
admin.site.register(Notice)