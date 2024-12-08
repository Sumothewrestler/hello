from django.contrib import admin
from .models import Thought

@admin.register(Thought)
class ThoughtAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at', 'updated_at')
    search_fields = ('content',)