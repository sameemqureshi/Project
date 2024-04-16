from django.contrib import admin


from .models import *

admin.site.register(Company)
admin.site.register(Entity)
admin.site.register(EntityData)

# Register your models here.
