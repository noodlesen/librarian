from django.contrib import admin
from app.models import Author, Book, Topic, Tag, Quote

# Register your models here.


class QuoteAdmin(admin.ModelAdmin):
    raw_id_fields=('tag',)
    autocomplete_lookup_fields = {
        'm2m': ['tag'],
    }


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Topic)
admin.site.register(Tag)
admin.site.register(Quote, QuoteAdmin)
