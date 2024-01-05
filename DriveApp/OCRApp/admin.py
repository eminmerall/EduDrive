from django.contrib import admin

from OCRApp.models import OCRDocument

class OCRDocumentAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'description')
    list_filter = ('user','title', 'description')
    search_fields = ('user','title', 'description')


admin.site.register(OCRDocument,OCRDocumentAdmin)