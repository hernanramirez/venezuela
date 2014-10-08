from django.contrib import admin
from estados_app.models import Estado, Municipio, Parroquia
# Register your models here.

admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Parroquia)
