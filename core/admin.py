from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(BookJournalBase)
class BookJournalBaseAdmin(admin.ModelAdmin):
    """ adding the product class to the admin site """

    list_display = (
        'name', "price", "description", "created_at")
    search_fields = ("name", "created_at")

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('num_pages', 'genre')
    search_fields = ("name", "category",)

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    """ adding the product class to the admin site """

    list_display = ("type", "publisher")
