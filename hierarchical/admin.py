from django.contrib import admin
from mptt.admin import DraggableModelAdmin
# Register your models here.

from hierarchical.models import Genre


admin.site.register(Genre, DraggableModelAdmin)
