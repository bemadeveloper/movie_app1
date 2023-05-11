from django.contrib import admin
from afisha import models

admin.site.register(models.Movie)
admin.site.register(models.Review)
admin.site.register(models.Director)


# Register your models here.