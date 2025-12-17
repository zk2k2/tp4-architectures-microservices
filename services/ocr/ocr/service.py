"""
OCR Service - Extraction de données depuis documents
Service partagé par Commercial et Risk Services
Technologies: Tesseract, AWS Textract
"""

class OCRService:
    """Service d'extraction OCR"""

    def __init__(self, ocr_engine):
        self.ocr_engine = ocr_engine  # Tesseract ou AWS Textract

    def extract_text(self, document_content):
        """Extrait le texte brut d'un document"""
        pass

    def extract_structured_data(self, document_content, document_type):
        """
        Extrait des données structurées selon le type
        document_type: PAYSLIP, BANK_STATEMENT, ID_CARD, etc.
        """
        pass

    def extract_payslip_data(self, document_content):
        """Extrait: revenus, employeur, période"""
        pass

    def extract_bank_statement_data(self, document_content):
        """Extrait: soldes, dépenses, revenus"""
        pass


class PayslipData:
    """Données extraites d'une fiche de paie"""
    def __init__(self):
        self.monthly_income = None
        self.employer_name = None
        self.employment_status = None  # CDI, CDD, etc.
        self.payment_date = None


class BankStatementData:
    """Données extraites d'un relevé bancaire"""
    def __init__(self):
        self.average_balance = None
        self.monthly_expenses = None
        self.monthly_income = None
        self.statement_period = None
