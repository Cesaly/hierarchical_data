from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
# Register your models here.

from hierarchical.models import Desserts


admin.site.register(Desserts, DraggableMPTTAdmin)
