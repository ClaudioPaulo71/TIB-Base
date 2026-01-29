from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import BatchRecord

def review_dashboard(request, record_id):
    # Busca o registro
    record = get_object_or_404(BatchRecord, id=record_id)
    
    # LÓGICA DO BOTÃO SALVAR (POST)
    if request.method == 'POST':
        # Captura os dados do formulário
        record.batch_number = request.POST.get('batch_number')
        record.document_no = request.POST.get('document_no')
        record.project_code = request.POST.get('project_code')
        record.issue_date = request.POST.get('issue_date')
        
        # Salva no banco de dados
        record.save()
        
        # Mensagem de sucesso (Feedback visual)
        messages.success(request, f"Registro {record.batch_number} atualizado e aprovado com sucesso!")
        
        # Recarrega a página limpa
        return redirect('review_dashboard', record_id=record.id)

    # LÓGICA DE EXIBIR (GET)
    return render(request, 'pharma_reader/review.html', {
        'record': record
    })