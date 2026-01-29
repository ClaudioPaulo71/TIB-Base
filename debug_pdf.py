import pdfplumber
import re
import glob
import os

# 1. Encontra o arquivo PDF mais recente que você subiu
list_of_files = glob.glob('media/batch_records/*.pdf')
if not list_of_files:
    print("ERRO: Nenhum arquivo PDF encontrado na pasta media/batch_records/")
    exit()

latest_file = max(list_of_files, key=os.path.getctime)
print(f"--> Analisando o arquivo: {latest_file}")

# 2. Abre e extrai o texto cru
try:
    with pdfplumber.open(latest_file) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        
        print("\n=== O QUE O ROBÔ ESTÁ VENDO (Início) ===")
        # Mostra os primeiros 600 caracteres para a gente ler
        print(text[:600]) 
        print("========================================\n")

        # 3. Testa o Regex ao vivo
        print("--> Testando Regex de Batch Number...")
        # Regex original
        match = re.search(r"Batch Number:\s*(\d+)", text, re.IGNORECASE)
        
        if match:
            print(f"SUCESSO! Encontrado: '{match.group(1)}'")
        else:
            print("FALHA: O padrão 'Batch Number:' seguido de números não foi encontrado.")
            
            # Tenta achar onde está a palavra Batch Number para ajudar
            if "Batch Number" in text:
                print("DICA: A frase 'Batch Number' EXISTE no texto. O problema é o que vem depois dela.")
            else:
                print("ERRO CRÍTICO: Nem a frase 'Batch Number' foi encontrada no texto extraído.")

except Exception as e:
    print(f"Erro ao abrir PDF: {e}")
