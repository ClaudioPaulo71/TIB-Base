# apps/pharma_reader/admin.py
from django.contrib import admin
from .models import BatchRecord

@admin.register(BatchRecord)
class BatchRecordAdmin(admin.ModelAdmin):
    # Colunas que aparecem na lista
    list_display = ('id', 'batch_number', 'document_no', 'uploaded_at', 'pdf_file')
    # Campos que são apenas leitura (para ninguém editar o que a IA extraiu manualmente sem querer)
    readonly_fields = ('batch_number', 'document_no', 'extracted_text')