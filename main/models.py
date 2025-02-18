from django.db import models
from django.core.validators import FileExtensionValidator 


# Notices 
class Notice(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pdf = models.FileField(upload_to='notices/', validators=[
        FileExtensionValidator(allowed_extensions=['pdf'])
    ])
    date = models.DateField()
    highlight = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Notices'
    
    def __str__(self):
        return self.title


# Gallery Catagory 
class GalleryCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Gallery Categories'

        
    def __str__(self):
        return self.name
    
# Gallery Items 
class GalleryItem(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

# Alumni
class Alumni(models.Model):
    name = models.CharField(max_length=100)
    batch_year = models.IntegerField()
    current_position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='alumni_photos/', null=True, blank=True)
    linkedin_url = models.URLField(blank=True)
    github = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    display = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-batch_year', 'name']
        verbose_name_plural = 'Alumni'
    
    def __str__(self):
        return f"{self.name} - Batch {self.batch_year}"

