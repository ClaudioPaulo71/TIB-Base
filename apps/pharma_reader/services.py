# apps/pharma_reader/services.py
import pdfplumber
import re
import os

def extract_data_from_pdf(record):
    path = record.pdf_file.path
    if not os.path.exists(path):
        return

    with pdfplumber.open(path) as pdf:
        text = pdf.pages[0].extract_text()
        record.extracted_text = text

        # 1. BATCH NUMBER
        batch_match = re.search(r"Batch Number:\s*(\d+)", text, re.IGNORECASE)
        if batch_match:
            record.batch_number = batch_match.group(1)

        # 2. DOCUMENT NO
        doc_match = re.search(r"Document No:[\s\"]*([\w-]+)", text, re.IGNORECASE)
        if doc_match:
            record.document_no = doc_match.group(1)

        # 3. PROJECT CODE
        proj_match = re.search(r"Project Code:\s*([\d-]+)", text, re.IGNORECASE)
        if proj_match:
            record.project_code = proj_match.group(1)

        # 4. DATA (Estratégia Blindada)
        # Regex explicaçao:
        # Effective Date: -> Procura a frase
        # \s* -> Aceita qualquer espaço depois
        # ([^\s]+)        -> O SEGREDO: Pega TUDO que não for espaço/enter (pega a data inteira)
        effective_date_match = re.search(r"Effective Date:\s*([^\s]+)", text, re.IGNORECASE)
        
        # Regex de backup (formato com barra)
        slash_date_match = re.search(r"(\d{1,2}/\d{1,2}/\d{2,4})", text)

        if effective_date_match:
            # Limpa sujeira caso venha algo grudado
            raw_date = effective_date_match.group(1).strip()
            record.issue_date = raw_date
            print(f"--> Data encontrada (Effective): {record.issue_date}")
        elif slash_date_match:
            record.issue_date = slash_date_match.group(1)
            print(f"--> Data encontrada (Genérica): {record.issue_date}")

        # Salva
        record.save(update_fields=['batch_number', 'document_no', 'project_code', 'issue_date', 'extracted_text'])