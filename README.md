
# 💊 TIB Pharma | Batch Record Review AI

> **Intelligent Pharmaceutical Auditing System**
> Automating the extraction, validation, and review of batch records for the regulated industry.

---

## 🎯 Project Objective
To transform the quality assurance (QA) review process, which is currently manual and prone to errors, into a digital workflow assisted by AI. The system ingests scanned PDF documents, extracts critical data (Batch Number, Dates, Codes) using advanced regex patterns, and presents a "Side-by-Side" auditing interface for human approval.

## 🚀 Current Features (v0.1 - MVP)
- **PDF Ingestion:** Upload of scanned Batch Records.
- **Intelligent Extraction:** Python engine (`pdfplumber` + Regex) that identifies:
- Batch Number
- Issue/Effective Date
- Project Code
- Document Number
- **Auditing Dashboard:** Split-screen interface (PDF vs. Data) for quick review.
- **Approval Workflow:** Editing of extracted data and persistence in the database.

## 🛠️ Tech Stack
- **Backend:** Python 3.13 + Django 5.x
- **Frontend:** Bootstrap 5 + Django Templates
- **Data Processing:** PDFPlumber, Re (Regex)
- **Database:** SQLite (Dev) / PostgreSQL (Prod ready)

## ⚙️ Installation and Execution

1. **Clone the repository:**
```bash
git clone [https://github.com/YOUR-USERNAME/tib-pharma-ai.git](https://github.com/YOUR-USERNAME/tib-pharma-ai.git)
cd tib-pharma-ai
```

#==================================================================================================================
# 💊 TIB Pharma | Batch Record Review AI

> **Sistema Inteligente de Auditoria Farmacêutica**
> Automatizando a extração, validação e revisão de registros de lotes (Batch Records) para a indústria regulada.

---

## 🎯 Objetivo do Projeto
Transformar o processo de revisão de qualidade (QA), que hoje é manual e propenso a erros, em um fluxo digital assistido por IA. O sistema ingere documentos PDF digitalizados, extrai dados críticos (Lote, Datas, Códigos) usando padrões regex avançados e apresenta uma interface de auditoria "Lado a Lado" para aprovação humana.

## 🚀 Funcionalidades Atuais (v0.1 - MVP)
- **Ingestão de PDF:** Upload de Batch Records digitalizados.
- **Extração Inteligente:** Motor Python (`pdfplumber` + Regex) que identifica:
  - Número do Lote (Batch Number)
  - Data de Emissão/Efetiva
  - Código do Projeto
  - Número do Documento
- **Painel de Auditoria:** Interface Split-Screen (PDF vs Dados) para conferência ágil.
- **Workflow de Aprovação:** Edição de dados extraídos e persistência em banco de dados.

## 🛠️ Tech Stack
- **Backend:** Python 3.13 + Django 5.x
- **Frontend:** Bootstrap 5 + Django Templates
- **Processamento de Dados:** PDFPlumber, Re (Regex)
- **Banco de Dados:** SQLite (Dev) / PostgreSQL (Prod ready).

## ⚙️ Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/tib-pharma-ai.git](https://github.com/SEU-USUARIO/tib-pharma-ai.git)
   cd tib-pharma-ai
