from django.contrib import admin

from . import models

admin.site.register(models.Sede)
admin.site.register(models.Plan)
admin.site.register(models.Suscriptor)
admin.site.register(models.SuscriptoPorSede)
admin.site.register(models.SuscriptoPorPLan)
