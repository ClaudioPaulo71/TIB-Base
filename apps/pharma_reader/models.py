# apps/pharma_reader/models.py
from django.db import models
import os

class BatchRecord(models.Model):
    # Campos existentes
    pdf_file = models.FileField(upload_to='batch_records/', verbose_name="Arquivo PDF")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Upload")
    
    # --- DADOS EXTRAÍDOS ---
    batch_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="Batch Number")
    
    # NOVOS CAMPOS AQUI
    document_no = models.CharField(max_length=50, blank=True, null=True, verbose_name="Document No")
    project_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="Project Code")
    issue_date = models.CharField(max_length=20, blank=True, null=True, verbose_name="Issued Date")
    
    extracted_text = models.TextField(blank=True, null=True, verbose_name="Texto Extraído (Raw)")

    def __str__(self):
        return f"Lote {self.batch_number or '???'} ({self.document_no})"

    class Meta:
        verbose_name = "Registro de Lote"
        verbose_name_plural = "Registros de Lote"

    # Método SAVE "Nuclear" (Mantivemos igual)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # NOVA REGRA: Roda a extração se tiver arquivo E (faltar Lote OU faltar Data)
        # Assim ele tenta de novo se a data falhar na primeira vez
        if self.pdf_file and (not self.batch_number or not self.issue_date):
            try:
                from .services import extract_data_from_pdf
                # print para debug no terminal
                print(f"--- INICIANDO EXTRAÇÃO AUTOMÁTICA (Smart Retry) ---")
                extract_data_from_pdf(self)
            except Exception as e:
                print(f"ERRO NA EXTRAÇÃO: {e}")