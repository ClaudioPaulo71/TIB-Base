# apps/pharma_reader/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BatchRecord
from .services import extract_data_from_pdf

@receiver(post_save, sender=BatchRecord)
def trigger_pdf_extraction(sender, instance, created, **kwargs):
    """
    Sempre que um BatchRecord é criado (upload feito), 
    chama o serviço de extração.
    """
    if created and instance.pdf_file:
        extract_data_from_pdf(instance)